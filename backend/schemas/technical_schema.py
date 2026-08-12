from pydantic import BaseModel


class TechnicalAnalysis(BaseModel):
    company: str
    trend: str
    moving_average_analysis: str
    rsi_analysis: str
    macd_analysis: str
    volume_analysis: str
    overall_signal: str
    recommendation: str