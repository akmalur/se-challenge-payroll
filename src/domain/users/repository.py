# src/domain/users/repository

from .schema import UserSchema


class UserRepository(object):
    def __init__(self, db):
        self.db = db

    def save(self, doc):
        session = self.db.SESSION()
        user = UserSchema(**doc)

        try:
            session.add(user)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return doc

    def get_by_id(self, id):
        session = self.db.SESSION()

        try:
            user = session.query(UserSchema).filter(UserSchema.id == id).first()
        finally:
            session.close()
        if user == None:
            raise LookupError('Failed to locate user with email: {}'.format(id))
        else:
            return user.json()

    def find_by_email(self, email):
        session = self.db.SESSION()

        try:
            user = session.query(UserSchema).filter(UserSchema.email == email).first()
        finally:
            session.close()
        if user == None:
            return user
        else:
            return user.json()
