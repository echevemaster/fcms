#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":mod: fcms.manage' -- Program entry point
"""
import sys

import Flask
from flask.ext.script import Manager
from fcms.core.factory import (create_app as create_application)

app = flask.Flask(__name__)

def create_app():
    """ Create application 
    """
    create_application(app)