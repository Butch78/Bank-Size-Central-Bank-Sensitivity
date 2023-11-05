from fastapi import APIRouter, Query, Depends
from sqlmodel import Session

from app.utils.deps import get_session
from app import crud
from app.schema.restaurant import RestaurantsCreate, RestaurantsRead

router = APIRouter()


@router.post("", response_model=RestaurantsRead)
async def create_restaurant(
    *,
    session: Session = Depends(get_session),
    restaurant: RestaurantsCreate,
) -> RestaurantsRead:
    print(restaurant)
    return crud.restaurants.create(db=session, obj_in=restaurant)


@router.get("", response_model=list[RestaurantsRead] | None)
async def read_restaurants(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
) -> list[RestaurantsRead]:
    return crud.restaurants.get_multi(db=session, skip=offset, limit=limit)


@router.get("/{restaurant_id}", response_model=RestaurantsRead)
async def read_restaurant(
    *,
    session: Session = Depends(get_session),
    restaurant_id: int,
) -> RestaurantsRead:
    return crud.restaurants.get(db=session, id=restaurant_id)
