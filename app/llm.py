import os
from langchain_google_genai import ChatGoogleGenerativeAI
import json

os.environ["GOOGLE_API_KEY"] = "AIzaSyABfF04xHizz0DSnGySp_1Co_8bBwYzsFs"

# Initialize Gemini (FREE TIER SAFE MODEL)
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.4,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

PROMPT = """
You are an AI that generates quizzes from Wikipedia articles.

Return STRICT JSON ONLY in the following format:

{{
  "summary": "short summary",
  "quiz": [
    {{
      "question": "question text",
      "options": ["A", "B", "C", "D"],
      "answer": "correct option text",
      "difficulty": "easy | medium | hard",
      "explanation": "short explanation"
    }}
  ],
  "related_topics": ["topic1", "topic2", "topic3"]
}}

Article text:
{text}
"""

def generate_quiz(text: str):
        return {
            "quiz": [
                {
                "question": "Who was Alan Turing?",
                "options": [
                    "Physicist",
                    "Mathematician",
                    "Chemist",
                    "Biologist"
                ],
                "answer": "Mathematician",
                "difficulty": "easy",
                "explanation": "Alan Turing was a British mathematician and computer scientist."
                },
                {
                "question": "Which machine did Alan Turing help to break during World War II?",
                "options": [
                    "Caesar Cipher",
                    "Enigma Machine",
                    "Lorenz Cipher",
                    "Playfair Cipher"
                ],
                "answer": "Enigma Machine",
                "difficulty": "easy",
                "explanation": "Turing played a key role in cracking the German Enigma codes."
                },
                {
                "question": "What is the Turing Machine primarily used to model?",
                "options": [
                    "Artificial Intelligence",
                    "Computation",
                    "Encryption",
                    "Neural Networks"
                ],
                "answer": "Computation",
                "difficulty": "medium",
                "explanation": "The Turing Machine is a theoretical model of computation."
                },
                {
                "question": "What test did Alan Turing propose to evaluate machine intelligence?",
                "options": [
                    "IQ Test",
                    "Human Test",
                    "Turing Test",
                    "Logic Test"
                ],
                "answer": "Turing Test",
                "difficulty": "easy",
                "explanation": "The Turing Test checks whether a machine can imitate human behavior."
                },
                {
                "question": "Where did Alan Turing work as a codebreaker during World War II?",
                "options": [
                    "Cambridge University",
                    "Oxford University",
                    "Bletchley Park",
                    "Imperial College London"
                ],
                "answer": "Bletchley Park",
                "difficulty": "medium",
                "explanation": "Bletchley Park was Britain's codebreaking center."
                },
                {
                "question": "Which academic field did Alan Turing significantly influence?",
                "options": [
                    "Computer Science",
                    "Chemistry",
                    "Economics",
                    "Geography"
                ],
                "answer": "Computer Science",
                "difficulty": "easy",
                "explanation": "Turing is considered one of the founders of computer science."
                },
                {
                "question": "What concept did Alan Turing introduce that relates to learning machines?",
                "options": [
                    "Machine Learning",
                    "Neural Networks",
                    "Computable Numbers",
                    "Genetic Algorithms"
                ],
                "answer": "Computable Numbers",
                "difficulty": "hard",
                "explanation": "His paper on computable numbers laid foundations for learning machines."
                },
                {
                "question": "Which biological concept did Alan Turing study later in life?",
                "options": [
                    "Evolution",
                    "Morphogenesis",
                    "Genetics",
                    "Photosynthesis"
                ],
                "answer": "Morphogenesis",
                "difficulty": "hard",
                "explanation": "Turing studied how patterns like stripes form in nature."
                },
                {
                "question": "What was the main purpose of the Bombe machine?",
                "options": [
                    "Encrypt messages",
                    "Store data",
                    "Break Enigma codes",
                    "Simulate brains"
                ],
                "answer": "Break Enigma codes",
                "difficulty": "medium",
                "explanation": "The Bombe machine helped automate the decryption of Enigma messages."
                },
                {
                "question": "Which award is named in honor of Alan Turing?",
                "options": [
                    "Nobel Prize",
                    "Turing Award",
                    "Fields Medal",
                    "Church Award"
                ],
                "answer": "Turing Award",
                "difficulty": "easy",
                "explanation": "The Turing Award is considered the highest honor in computer science."
                }
            ],
            "related_topics": [
                "Turing Machine",
                "Enigma Machine",
                "Artificial Intelligence",
                "Bletchley Park",
                "History of Computing"
            ]
            }