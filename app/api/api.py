from fastapi import APIRouter
from app.api.api_v1.deposit_rates import router as deposit_rates_router
from app.api.api_v1.target_rates import router as target_rates_router
from app.api.api_v1.target_ranges import router as target_ranges_router


api_router = APIRouter()

api_router.include_router(deposit_rates_router, prefix="/deposit_rates", tags=["deposit_rates"])
api_router.include_router(target_rates_router, prefix="/target_rates", tags=["target_rates"])
api_router.include_router(target_ranges_router, prefix="/target_ranges", tags=["target_ranges"])

