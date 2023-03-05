from pydantic import EmailStr

class User():
    id: int
    email: EmailStr
    password: str
    status: str
    