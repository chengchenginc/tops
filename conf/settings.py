#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

CONFIG_PATH = os.path.dirname(os.path.abspath(__file__)) if "__file__" in locals() else os.getcwd()
DATA_PATH = os.path.dirname(CONFIG_PATH)+os.path.sep+"data"+os.path.sep