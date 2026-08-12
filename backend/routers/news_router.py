from fastapi import APIRouter

from schemas.request_schema import SymbolRequest
from agents.news_agent import NewsAgent

router = APIRouter()

agent = NewsAgent()


@router.post("/")
def analyze_news(request: SymbolRequest):
    result = agent.analyze(request.symbol)
    return result.model_dump()