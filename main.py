from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Chief AI - Cooking Assistant")

# Allow frontend to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class Query(BaseModel):
    question: str

# Dummy AI response function (replace with real AI integration later)
def get_ai_response(question: str) -> str:
    return f"AI says: I can help you with '{question}'!"

@app.post("/ask")
def ask(query: Query):
    answer = get_ai_response(query.question)
    return {"answer": answer}

@app.get("/")
def root():
    return {"message": "Chief AI Backend Running!"}
