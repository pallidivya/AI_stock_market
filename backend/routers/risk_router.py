from fastapi import APIRouter

from agents.risk_agent import RiskAgent
from schemas.risk_schema import RiskRequest


router = APIRouter()

agent = RiskAgent()


@router.post("/")
def analyze_risk(request: RiskRequest):

    result = agent.analyze(request.symbol)

    return result.model_dump()