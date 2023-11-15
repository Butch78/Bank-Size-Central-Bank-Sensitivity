from app.crud.base import CRUDBase

from app.schema.restaurant import Restaurants, RestaurantsCreate, RestaurantsUpdate

from app.schema.target_range import TargetRanges, TargetRangesCreate, TargetRangesUpdate

restaurants = CRUDBase[Restaurants, RestaurantsCreate, RestaurantsUpdate](Restaurants)
target_ranges = CRUDBase[TargetRanges, TargetRangesCreate, TargetRangesUpdate](TargetRanges)
