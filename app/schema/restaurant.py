from typing import Union
from sqlmodel import SQLModel, Field
from typing import Optional


class RestaurantsBase(SQLModel):
    name: str
    address: Union[str, None] = None


class Restaurants(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: Union[str, None] = None

    class Config:
        from_attributes = True


# Pydantic model
class RestaurantsCreate(RestaurantsBase):
    name: str
    address: Union[str, None] = None


class RestaurantsRead(RestaurantsBase):
    pass


class RestaurantsUpdate(RestaurantsBase):
    pass
