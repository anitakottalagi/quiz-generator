from sqlalchemy import Column, Integer, String, Text, JSON
from .database import Base

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    title = Column(String)
    summary = Column(Text)
    key_entities = Column(JSON)  # Dict with people, organizations, locations
    sections = Column(JSON)      # List of section titles
    quiz = Column(JSON)          # List of quiz questions
    related_topics = Column(JSON)  # List of topics