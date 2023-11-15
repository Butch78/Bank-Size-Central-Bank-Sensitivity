from app.crud.base import CRUDBase

from app.schema.restaurant import Restaurants, RestaurantsCreate, RestaurantsUpdate
from app.schema.target_range import TargetRanges, TargetRangesCreate, TargetRangesUpdate
from app.schema.deposit_rate import DepositRates, DepositRatesCreate, DepositRatesUpdate

restaurants = CRUDBase[Restaurants, RestaurantsCreate, RestaurantsUpdate](Restaurants)
target_ranges = CRUDBase[TargetRanges, TargetRangesCreate, TargetRangesUpdate](
    TargetRanges
)
deposit_rates = CRUDBase[DepositRates, DepositRatesCreate, DepositRatesUpdate](
    DepositRates
)
