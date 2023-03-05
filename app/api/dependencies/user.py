
from datetime import datetime
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from app.core.hashing import verify_password
from app.repositories.db.users import find_user_by_filter
from app.models.users import User
from app.schemas.users import UserCreate, UserConfirmCode
from app.constants.user import STATUS

security = HTTPBasic()

async def basic_authentication(credentials: HTTPBasicCredentials = Depends(security)) -> User:
    user = await find_user_by_filter({"email": credentials.username })
    if not (user and verify_password(credentials.password, user.password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user

async def verify_code_confirmation(body: UserConfirmCode, user: User = Depends(basic_authentication)) -> User:
    if (user.status != STATUS["pending"]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Email already verified",
        )

    now = datetime.today().timestamp()
    if (user.code_expiration < now):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The code has expired",
        )

    if (user.code != int(body.code)):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong code",
        )
    
    return user


async def unique_user(user: UserCreate) -> User:
    already_exist = await find_user_by_filter({"email": user.email})
    if already_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists",
        )
    return user