from app.crud.base import CRUDBase

from app.schema.target_range import TargetRanges, TargetRangesCreate, TargetRangesUpdate

class CRUDTargetRanges(CRUDBase[TargetRanges, TargetRangesCreate, TargetRangesUpdate]):
    pass
    
target_ranges = CRUDTargetRanges(TargetRanges)