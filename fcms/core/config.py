# -*- coding: utf-8 -*-

import os
basedir = os.path.split(os.path.abspath(os.path.dirname('__file__')))[0]


class Config(object):
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Base config for production environment
    """
    pass   # for now


class DevelopmentConfig(Config):
    """ Base Config for development environment
    """
    DEBUG = True
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                              'db', 'fcms.db')
    SQLALCHEMY_ECHO = True
    DATABASE_CONNECT_OPTIONS = {}
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'your-session-key'


class TestingConfig(config):
    """ Base config for testing environment
    """
    TESTING = True
