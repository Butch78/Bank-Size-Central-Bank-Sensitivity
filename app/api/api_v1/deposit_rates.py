from fastapi import APIRouter, Query, Depends
from sqlmodel import Session

from app.utils.deps import get_session
from app import crud
from app.schema.deposit_rate import DepositRatesCreate, DepositRatesRead

router = APIRouter()


@router.post("", response_model=DepositRatesRead)
async def create_deposit_rate(
    *,
    session: Session = Depends(get_session),
    deposit_rate: DepositRatesCreate,
) -> DepositRatesRead:
    print(deposit_rate)
    return crud.deposit_rates.create(db=session, obj_in=deposit_rate)


@router.get("", response_model=list[DepositRatesRead] | None)
async def read_deposit_rates(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
) -> list[DepositRatesRead]:
    return crud.deposit_rates.get_multi(db=session, skip=offset, limit=limit)


@router.get("/{deposit_rate_id}", response_model=DepositRatesRead)
async def read_deposit_rate(
    *,
    session: Session = Depends(get_session),
    deposit_rate_id: int,
) -> DepositRatesRead:
    return crud.deposit_rates.get(db=session, id=deposit_rate_id)
