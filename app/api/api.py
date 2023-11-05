from fastapi import APIRouter

from app.api.api_v1.restaurants import router as restaurants_router

api_router = APIRouter()
api_router.include_router(
    restaurants_router, prefix="/restaurants", tags=["restaurants"]
)
