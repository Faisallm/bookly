from fastapi import FastAPI
from .books import routes
# to define which code will at start and end of...
# application. i.e the application lifespan.
from contextlib import asynccontextmanager
from .db.main import init_db, main
import asyncio



@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"server is starting ...")
    print(f"Connecting to db...")
    await init_db()
    yield
    print(f"Disconnecting from db...")
    print(f"server has been stopped")


version = "v1"

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version,
    lifespan=life_span
)

app.include_router(routes.book_router, prefix=f"/api/{version}/books",
                   tags=["books"])