from src.models import Summary
from src.schemas import Prompt

from fastapi import APIRouter
from src.services import GroqService
router = APIRouter()
groq_service = GroqService()

# Summarizer
@router.post("/api/summarizer", response_model=Summary)
def NewsAnalyzer(news: Prompt):
    result = groq_service.analyze_news(news)
    return result









