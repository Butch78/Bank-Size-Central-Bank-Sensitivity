from fastapi import APIRouter, Query, Depends
from sqlmodel import Session

from app.utils.deps import get_session
from app import crud
from app.schema.target_range import TargetRangesCreate, TargetRangesRead

router = APIRouter()


@router.post("", response_model=TargetRangesRead)
async def create_target_ranges(
    *,
    session: Session = Depends(get_session),
    target_ranges: TargetRangesCreate,
) -> TargetRangesRead:
    print(target_ranges)
    return crud.target_ranges.create(db=session, obj_in=target_ranges)


@router.get("", response_model=list[TargetRangesRead] | None)
async def read_target_ranges(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
) -> list[TargetRangesRead]:
    return crud.target_ranges.get_multi(db=session, skip=offset, limit=limit)


@router.get("/{target_rate_id}", response_model=TargetRangesRead)
async def read_target_rate(
    *,
    session: Session = Depends(get_session),
    target_rate_id: int,
) -> TargetRangesRead:
    return crud.target_ranges.get(db=session, id=target_rate_id)
