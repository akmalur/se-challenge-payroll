# config.py

class Config(object):
    """
    Common configurations
    """

class TestConfig(Config):
    """
    Testing configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'tests': TestConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}