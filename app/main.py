from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.utils.config import settings
from app.utils.deps import create_db_and_tables
from app.api.api import api_router

app = FastAPI()


app.on_event("startup")
async def startup_event():
    create_db_and_tables()


@app.on_event("shutdown")
async def on_shutdown():
    pass


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(api_router)

    return _app


app = get_application()


@app.get("/")
def root():
    return "Welcome to the FastAPI and Postgres in a dev container demonstration. Add /docs to the URL to see API methods."
