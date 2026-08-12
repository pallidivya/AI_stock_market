from fastapi import FastAPI

from routers.report_router import router as report_router
from routers.advisor_router import router as advisor_router
from routers.portfolio_router import router as portfolio_router
from routers.news_router import router as news_router
from routers.technical_router import router as technical_router
from routers.risk_router import router as risk_router
from routers.financial_router import router as financial_router

app = FastAPI(
    title="AI Stock Market Research API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Stock Market Research API is Running!"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }

app.include_router(
    news_router,
    prefix="/news",
    tags=["News"]
)

app.include_router(
    technical_router,
    prefix="/technical",
    tags=["Technical"]
)

app.include_router(
    financial_router,
    prefix="/financial",
    tags=["Financial Analysis"]
)

app.include_router(
    risk_router,
    prefix="/risk",
    tags=["Risk Analysis"]
)

app.include_router(
    portfolio_router,
    prefix="/portfolio",
    tags=["Portfolio"]
)

app.include_router(
    advisor_router,
    prefix="/advisor",
    tags=["Investment Advisor"]
)

app.include_router(
    report_router,
    prefix="/report",
    tags=["Daily Report"]
)