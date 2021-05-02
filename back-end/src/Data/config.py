import os

class AppSetting(object):

    DEBUG = False
    TESTING = False
    # This file should be updated
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(AppSetting):
    DEBUG = False


class StagingConfig(AppSetting):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(AppSetting):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(AppSetting):
    TESTING = True