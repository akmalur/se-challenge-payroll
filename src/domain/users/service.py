# src/domain/users/service.py

from .user import User


class UserService(object):
    def __init__(self, repository):
        self.repository = repository

    def createUser(self, email, password):
        user = User(email)
        user.password = password

        return self.repository.save(user.json())

    def getUserByID(self, id):
        doc = self.repository.get_by_id(id)
        return User(**doc)

    def findUserByEmail(self, email):
        doc = self.repository.find_by_email(email)
        if doc == None:
            return None
        else:
            return User(**doc)