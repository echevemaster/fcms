# -*- coding: utf-8 -*-

from flask import current_app
from fcms.core.database import db


def create_app(app):
    """Create app and return application object
    Keyword arguments:
    app -- application object

    """
    app.config.from_object('fcms.core.config.DevelopmentConfig')
    db.init_app
