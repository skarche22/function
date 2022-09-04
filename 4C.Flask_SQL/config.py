class Config(object):

    """ common configuration """
    # put any configuration here that are common across all environment
    SECRET_KEY='sk-works2022'

    SQLALCHEMY_DATABASE_URI = "mysql://root:root123@localhost/user_info"
    SQLALCHEMY_TRACK_MODIFICATION = False

class DevelopementConfig(Config):
    """ Developement configuration """
    DEBUG = True
    SQLCHEMY_ECHO = True

class TestingConfig(Config):
    """ Testing configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = True
    SQLALCHEMY_TRACK_MODIFICATION = False



class ProductionConfig(Config):
    """ Production configuration"""
    DEBUG = False


class Productionconfig:
    pass


app_config = {
    'developement': DevelopementConfig,
    'testing':TestingConfig,
    'production':Productionconfig
}




