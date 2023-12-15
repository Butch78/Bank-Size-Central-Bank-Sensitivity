from fastapi import APIRouter, Query, Depends
from sqlmodel import Session

from app.utils.deps import get_session
from app import crud
from app.schema.target_rate import TargetRatesCreate, TargetRatesRead, TargetRatesCreateOut

router = APIRouter()


@router.post("", response_model=TargetRatesCreateOut)
async def create_target_rates(
    *,
    session: Session = Depends(get_session),
    target_rates: TargetRatesCreate,
) -> TargetRatesCreateOut:
    print(target_rates)
    return crud.target_rates.create(db=session, obj_in=target_rates)


@router.get("", response_model=list[TargetRatesRead] | None)
async def read_target_rates(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
) -> list[TargetRatesRead]:
    return crud.target_rates.get_multi(db=session, skip=offset, limit=limit)


@router.get("/{target_rate_id}", response_model=TargetRatesRead)
async def read_target_rate(
    *,
    session: Session = Depends(get_session),
    target_rate_id: int,
) -> TargetRatesRead:
    return crud.target_rates.get(db=session, id=target_rate_id)
