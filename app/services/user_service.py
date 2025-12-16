from app.models.user_model import UserModel

users = []

class UserService:
    @staticmethod
    def create_user(name: str, email: str, password: str) -> UserModel:
        user = UserModel(id=len(users)+1, name=name, email=email, password=password)
        users.append(user)
        return user