# src/domain/users/__init__.py

from .repository import UserRepository
from .service import UserService


def createUserService(db):
    user_repository = UserRepository(db)
    return UserService(user_repository)