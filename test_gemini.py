import os
import google.generativeai as genai

# Check API key
api_key = os.getenv("GOOGLE_API_KEY")
print("API KEY FOUND:", bool(api_key))

# Configure Gemini
genai.configure(api_key=api_key)

# List available models
models = genai.list_models()
print("\nAvailable models:\n")

for model in models:
    print(model.name)