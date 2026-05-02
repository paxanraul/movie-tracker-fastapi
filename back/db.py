from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

DATABASE_URL = "postgresql+asyncpg://paxan_raul:123456@localhost:5432/movie_db"

engine = create_async_engine(DATABASE_URL)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


# Создает таблицу
async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)