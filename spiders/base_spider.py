#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import requests
import time, datetime
import re
import html
import json
from bs4 import BeautifulSoup

headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "application/json"}

tag_regex = r'<[^>]+>'
tag_rc = re.compile(tag_regex, re.S)


def filter_tags(htm):
    htm = html.unescape(htm)
    text = tag_rc.sub('', htm)
    return text

class SpiderApi(object):

    # 转义字符串
    @classmethod
    def escape_string(cls, val):
        return pymysql.escape_string(str(val))

    @classmethod
    def get_hots(cls):
        pass

