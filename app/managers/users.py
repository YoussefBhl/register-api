from app.builders.query import Query
from app.core.config import database
from app.models.users import User


async def find_one_by_filter(filters: dict) -> User:
    query_builer = Query("users")
    qb = query_builer    \
    .add_select("id")   \
    .add_select("email") \
    .add_select("status") \
    .add_select("password") \
    .add_select("code") \
    .add_select("code_expiration")
    for key in list(filters.keys()):
        qb = qb.add_condition(key)
    query = qb.and_where().select_query()
    return await database.fetch_one(query, filters)

async def create_one(values: dict) -> User:
    query_builer = Query("users")
    query = query_builer.insert_query(values)
    return await database.execute(query=query, values=values)

async def update_one(id: int, values: dict) -> User:
    query_builer = Query("users")
    query = query_builer.update_query(values)
    return await database.execute(query=query, values={"id": id, **values})