# src/common/database

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Database(object):
    ENGINE = None
    MODEL = declarative_base()
    SESSION = None

    @staticmethod
    def initialize(url):
        Database.ENGINE = sqlalchemy.create_engine(url, client_encoding='utf8')
        Database.MODEL.metadata.create_all(Database.ENGINE)
        Database.SESSION = sessionmaker(bind=Database.ENGINE)
