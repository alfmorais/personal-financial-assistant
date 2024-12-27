from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.app.user_management.views import router as user_management_routers
from src.infrastructure.database.utils import create_database_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database_and_tables()
    yield


app = FastAPI(
    title="Personal Financial Assistant API",
    description="An intelligent API to manage and organize your personal finances",  # noqa E501
    lifespan=lifespan,
)
app.include_router(user_management_routers, prefix="/api/v1")
