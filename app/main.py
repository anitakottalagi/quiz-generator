from fastapi import FastAPI,Form, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .database import get_db, engine, Base
from .models import Quiz
from .scraper import scrape_wikipedia
from .llm import generate_quiz

Base.metadata.create_all(bind=engine)

app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")  # For CSS/JS if needed
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    past_quizzes = db.query(Quiz.id, Quiz.title).order_by(Quiz.id.desc()).all()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "past_quizzes": past_quizzes
        }
    )

@app.post("/generate-quiz")
async def generate_quiz_endpoint(url: str=Form(...), db: Session = Depends(get_db)):
    print("URL recieved",url)

        # Scrape
    scraped = scrape_wikipedia(url)
        
        # Generate quiz
    llm_output = generate_quiz(scraped["full_text"])
        # Prepare data
    data = {
            "url": url,
            "title": scraped["title"],
            "summary": scraped["summary"],
            "key_entities": scraped["key_entities"],
            "sections": scraped["sections"],
            "quiz": llm_output.get("quiz", []),
            "related_topics": llm_output.get("related_topics", [])
        }

        #Store in DB
    quiz = Quiz(**data)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
        
    data["id"] = quiz.id
    return data
    

@app.get("/quizzes")
def get_quizzes():
    return {
        "quizzes": [
            {
                "id": 1,
                "title": "Alan Turing Quiz",
                "created_at": "2024-01-10"
            }
        ]
    }    

@app.get("/quiz/{quiz_id}")
async def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz