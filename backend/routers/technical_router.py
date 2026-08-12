from fastapi import APIRouter

from schemas.request_schema import SymbolRequest
from agents.technical_agent import TechnicalAgent

router = APIRouter()

agent = TechnicalAgent()


@router.post("/")
def analyze_technical(request: SymbolRequest):
    result = agent.analyze(request.symbol)
    return result.model_dump()