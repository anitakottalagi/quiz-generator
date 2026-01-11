from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-pro-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

print(llm.invoke("Say hello"))