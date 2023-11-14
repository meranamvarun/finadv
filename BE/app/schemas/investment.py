from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class InvestmentBase(BaseModel):
    user_id: int
    platform_id: str
    invest_type: str
    name: str
    invested_time: datetime
    annual_return_rate: float
    expected_xor: float
    volatility: str


class InvestmentCreate(InvestmentBase):
    pass


class InvestmentUpdate(InvestmentBase):
    pass


class InvestmentInDBBase(InvestmentBase):
    id: int

    class Config:
        orm_mode = True


class Investment(InvestmentInDBBase):
    pass


class InvestmentInDB(InvestmentInDBBase):
    pass


class InvestmentOut(BaseModel):
    id: int
    user_id: int
    platform_id: str
    invest_type: str
    name: str
    invested_time: datetime
    annual_return_rate: Optional[float] = None
    expected_xor: Optional[float] = None
    volatility: str

    class Config:
        orm_mode = True
