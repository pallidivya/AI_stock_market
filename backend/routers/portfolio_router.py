from fastapi import APIRouter
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from agents.portfolio_agent import PortfolioAgent


router = APIRouter()

agent = PortfolioAgent()


class PortfolioRequest(BaseModel):
    symbols: list[str]


@router.post("/")
def analyze_portfolio(request: PortfolioRequest):

    result = agent.analyze(request.symbols)

    return result.model_dump()