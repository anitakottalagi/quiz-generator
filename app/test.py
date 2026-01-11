import google.generativeai as genai
import os


genai.configure(api_key=os.environ["AIzaSyABfF04xHizz0DSnGySp_1Co_8bBwYzsFs"])

models = genai.list_models()
for m in models:
    print(m.name)