from pydantic import BaseModel


class SymbolRequest(BaseModel):
    symbol: str


class FinancialRequest(BaseModel):
    company: str
    pdf_path: str


class AdvisorRequest(BaseModel):
    symbol: str
    pdf_path: str


class ReportRequest(BaseModel):
    symbol: str
    pdf_path: str