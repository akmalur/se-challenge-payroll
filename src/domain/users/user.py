# src/domain/users/user
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def __init__(self, email, password_hash=None, id=None):
        self.email = email
        self.password_hash = password_hash
        self.id = id

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User: {}'.format(self.email)

    def json(self):
        return {
            'email': self.email,
            'id': self.id,
            'password_hash': self.password_hash
        }