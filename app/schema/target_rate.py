from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class TargetRatesBase(SQLModel):
    date: datetime = Field(..., description="The date of the record")
    value: float = Field(..., description="The value of the SNB policy rate target")


class TargetRates(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(..., description="The date of the record")
    value: float = Field(..., description="The value of the SNB policy rate target")

    class Config:
        from_attributes = True


class TargetRatesCreate(TargetRatesBase):
    pass


class TargetRatesRead(TargetRatesBase):
    pass


class TargetRatesUpdate(TargetRatesBase):
    pass
