from typing import List
from pydantic import BaseModel


class NewsAnalysis(BaseModel):
    company: str
    summary: str
    sentiment: str
    important_events: List[str]
    impact: str
    risk: str
    recommendation: str