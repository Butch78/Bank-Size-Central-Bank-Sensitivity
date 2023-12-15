from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


from app.utils.config import settings
from app.utils.deps import create_db_and_tables, import_data, create_read_only_user
from app.api.api import api_router

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    import_data()
    create_read_only_user()

    yield


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return f"Welcome to the {settings.PROJECT_NAME} Application. Add /docs to the URL to see API methods."
