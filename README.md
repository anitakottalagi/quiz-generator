# Wikipedia Quiz Generator

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set up PostgreSQL database and update `DATABASE_URL` in `database.py`.
3. Add your Google AI API key in `llm.py`.
4. Run: `uvicorn app.main:app --reload`
5. Open http://127.0.0.1:8000

## Usage
- Enter a Wikipedia URL in TAB 1 and generate a quiz.
- Data is stored in DB and displayed in cards.
- TAB 2 is a placeholder for listing stored quizzes (extend as needed).