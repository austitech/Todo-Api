import os


BASEDIR = os.path.abspath(os.path.dirname(__name__))
print(BASEDIR)


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "default"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Config):
    SECRET_KEY = "AVeryLongRandomUnguessableString"


class Development(Config):
    SECRET_KEY = "DevelopmentIsNotSecurityConcious"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
        os.path.join(BASEDIR, "todo.db"))


class Testing(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(
        os.path.join(BASEDIR, "test.db"))
