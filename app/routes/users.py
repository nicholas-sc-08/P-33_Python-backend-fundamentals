from fastapi import APIRouter
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreateSchema

router = APIRouter()

@router.post("/users")
def create_user(user: UserCreateSchema):
    return UserService.create_user(user.name, user.email, user.password)