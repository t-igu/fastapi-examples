import asyncpg
from fastapi_app_django_fullskack.settings import DATABASES

db_config={
    "user":DATABASES["default"]["USER"],
    "password":DATABASES["default"]["PASSWORD"],
    "database":DATABASES["default"]["NAME"],
    # "database": "dvdrental",
    "host":DATABASES["default"]["HOST"],
    "port":DATABASES["default"]["PORT"],
    "min_size":3,
    "max_size":20
}

# asyncpg connection pool object
db_pool = None

async def create_pool():
    global db_pool
    db_pool = await asyncpg.create_pool(**db_config)
    # print(db_config)
    # async with db_pool.acquire() as connection:
    #     async with connection.transaction():
    #         [print(dict(record)) async for record in connection.cursor("select * from public.department")]

def terminate_pool():
    if db_pool:
        db_pool.terminate()

def get_connection():
    return db_pool

async def execute_query(query, params={}):
    async with db_pool.acquire() as connection:
        async with connection.transaction():
            return [dict(record) async for record in connection.cursor(query)]
