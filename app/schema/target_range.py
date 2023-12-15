from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class TargetRangesBase(SQLModel):
    date: datetime = Field(..., description="The date of the record")
    lower_bound: float = Field(
        ..., description="The lower bound of the SNB policy rate target"
    )
    upper_bound: float = Field(
        ..., description="The upper bound of the SNB policy rate target"
    )


class TargetRanges(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(..., description="The date of the record")
    lower_bound: float = Field(
        ..., description="The lower bound of the SNB policy rate target"
    )
    upper_bound: float = Field(
        ..., description="The upper bound of the SNB policy rate target"
    )

    class ConfigDict:
        from_attributes = True


class TargetRangesCreate(TargetRangesBase):
    pass


class TargetRangesRead(TargetRangesBase):
    pass

class TargetRangesCreateOut(TargetRangesCreate):
    id: int

class TargetRangesUpdate(TargetRangesBase):
    pass
