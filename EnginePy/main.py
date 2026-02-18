from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from meta_model import Procedure
from validator import validate_procedure
from generate_chatbot import generate_chatbot
from chatbot_engine import ask_question

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/validate")
def validate(proc: Procedure):
    errors = validate_procedure(proc)
    return {"valid": len(errors) == 0, "errors": errors}

@app.post("/generate")
def generate(proc: Procedure):
    errors = validate_procedure(proc)
    if errors:
        return {"valid": False, "errors": errors}
    chatbot_json = generate_chatbot(proc)
    return {"valid": True, "chatbot": chatbot_json}

@app.post("/chat")
def chat(payload: dict = Body(...)):
    # Ici on récupère le JSON correctement
    question = payload.get("question", "")
    chatbot_json = payload.get("chatbot_json", {})
    answer = ask_question(question, chatbot_json)
    return {"answer": answer}
