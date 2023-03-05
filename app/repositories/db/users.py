from datetime import datetime
from random import randrange

from app.core.hashing import get_password_hash
from app.managers.users import find_one_by_filter, create_one, update_one
from app.schemas.users import UserCreate
from app.models.users import User
from app.constants.user import STATUS, CODE_MIN, CODE_MAX, CODE_EXPIRE_IN


async def find_user_by_filter(filter: dict) -> User:
    return await find_one_by_filter(filter)

async def create_user(user: UserCreate) -> User:
    code_expiration = datetime.today().timestamp() + CODE_EXPIRE_IN
    code = randrange(CODE_MIN, CODE_MAX)
    values = {"email": user.email, "password": get_password_hash(user.password), "code": code, "code_expiration": code_expiration, "status": STATUS["pending"]}
    id = await create_one(values)
    return await find_user_by_filter({"id": id})

async def update_user(id: int, values: dict) -> User:
    await update_one(id, values)
    return await find_user_by_filter({"id": id})
