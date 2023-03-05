
from fastapi import APIRouter, Depends

from app.repositories.db.users import create_user, update_user
from app.repositories.emailing.stmp import mock_stmp
from app.schemas.users import UserCreate, UserConfirmCode, UserResponse
from app.models.users import User
from app.api.dependencies.user import unique_user, verify_code_confirmation
from app.constants.user import STATUS

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=UserResponse)
async def post_users(user: UserCreate = Depends(unique_user)) -> UserResponse:
    created_user = await create_user(user)
    await mock_stmp(created_user.code)
    return created_user

@router.post("/confirm-code/", response_model=UserResponse)
async def post_confirm_code(body: UserConfirmCode, user: User = Depends(verify_code_confirmation)) -> UserResponse:
    return await update_user(user.id, {"status": STATUS["verified"], "code": None, "code_expiration": None})
