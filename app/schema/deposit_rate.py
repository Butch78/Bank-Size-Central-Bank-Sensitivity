from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class DepositRatesBase(SQLModel):
    date: datetime = Field(..., description="The date of the record")
    value: float = Field(..., description="The actual deposit rate data")


class DepositRates(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(..., description="The date of the record")
    value: float = Field(..., description="The actual deposit rate data")

    class ConfigDict:
        from_attributes = True


class DepositRatesCreate(DepositRatesBase):
    pass

class DepositRatesCreateOut(DepositRatesCreate):
    id: int

class DepositRatesRead(DepositRatesBase):
    pass


class DepositRatesUpdate(DepositRatesBase):
    pass

