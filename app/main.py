from fastapi import FastAPI
from pydantic import BaseModel

from app.redactor import mask_pii
from app.llm_service import generate_response

app = FastAPI()

class UserInput(BaseModel):
    text: str


@app.post("/chat")

def chat(user_input: UserInput):

    cleaned = mask_pii(user_input.text)

    response = generate_response(cleaned)

    safe_output = mask_pii(response)

    return {
        "safe_response": safe_output
    }