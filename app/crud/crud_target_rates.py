from app.crud.base import CRUDBase

from app.schema.target_rate import TargetRates, TargetRatesCreate, TargetRatesUpdate


class CRUDTargetRates(CRUDBase[TargetRates, TargetRatesCreate, TargetRatesUpdate]):
    pass


target_rates = CRUDTargetRates(TargetRates)
