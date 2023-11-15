from app.crud.base import CRUDBase

from app.schema.deposit_rate import DepositRates, DepositRatesCreate, DepositRatesUpdate

class CRUDDepositRates(CRUDBase[DepositRates, DepositRatesCreate, DepositRatesUpdate]):
    pass

deposit_rates = CRUDDepositRates(DepositRates)
