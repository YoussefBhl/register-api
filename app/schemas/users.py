from pydantic import BaseModel, EmailStr, StrictInt, validator
from app.constants.user import CODE_MIN, CODE_MAX

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserConfirmCode(BaseModel):
    code: StrictInt
    
    @validator("code")
    def code_validator(cls, value) -> int:
        if (value < CODE_MIN or value > CODE_MAX):
            raise ValueError("value is not a 4 digit code")
        return value

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    status: str
