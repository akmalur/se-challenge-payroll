# src/domain/users/schema

from sqlalchemy import Column, Integer, String

from src.common.database import Database


class UserSchema(Database.MODEL):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column("email", String, unique=True)
    password_hash = Column("password", String)

    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'password_hash': self.password_hash
        }