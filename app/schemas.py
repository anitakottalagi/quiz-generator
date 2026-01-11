from pydantic import BaseModel
from typing import List, Dict


class QuizQuestion(BaseModel):
    question: str
    options: Dict[str, str]
    correct_answer: str
    difficulty: str
    explanation: str


class QuizOutput(BaseModel):
    quiz: List[QuizQuestion]
    related_topics: List[str]