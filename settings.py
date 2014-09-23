# -*- coding:utf-8 -*-

import sys
import os

from dao.PostgresDaoFactory import PostgresDaoFactory

FACTORY = PostgresDaoFactory()
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(PROJECT_PATH)
