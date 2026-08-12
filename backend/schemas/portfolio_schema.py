from typing import List
from pydantic import BaseModel, Field


class StockAllocation(BaseModel):
    symbol: str = Field(description="Stock symbol")
    allocation_percent: float = Field(
        description="Suggested portfolio allocation percentage"
    )


class PortfolioAnalysis(BaseModel):
    portfolio_summary: str

    diversification: str

    overall_risk: str

    strongest_stock: str

    weakest_stock: str

    suggested_allocations: List[StockAllocation]

    recommendation: str