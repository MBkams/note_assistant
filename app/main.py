import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI()

class Prompt(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/chat")
def chat_with_gemini(prompt: Prompt):
    response = model.generate_content(prompt.text)
    return {"response": response.text}
