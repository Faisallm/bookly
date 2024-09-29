from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from src.config import Config


engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True
)

# the right time to connect to the db...
# is when the db is starting.


async def init_db():
    async with engine.begin() as conn:
        statement = text("SELECT 'imittis';")

        result = await conn.execute(statement)

        print(result.all())

