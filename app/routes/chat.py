from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm_service import get_ai_response

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(req: ChatRequest):
    return get_ai_response(req.question)
