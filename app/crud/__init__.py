from app.crud.base import CRUDBase

from app.schema.deposit_rate import DepositRates, DepositRatesCreate, DepositRatesUpdate
from app.schema.restaurant import Restaurants, RestaurantsCreate, RestaurantsUpdate
from app.schema.target_range import TargetRanges, TargetRangesCreate, TargetRangesUpdate
from app.schema.target_rate import TargetRates, TargetRatesCreate, TargetRatesUpdate


deposit_rates = CRUDBase[DepositRates, DepositRatesCreate, DepositRatesUpdate](
    DepositRates
)

restaurants = CRUDBase[Restaurants, RestaurantsCreate, RestaurantsUpdate](Restaurants)
target_ranges = CRUDBase[TargetRanges, TargetRangesCreate, TargetRangesUpdate](
    TargetRanges
)
target_rates = CRUDBase[TargetRates, TargetRatesCreate, TargetRatesUpdate](TargetRates)
