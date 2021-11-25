#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from spiders.base_spider import *

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__)) if "__file__" in locals() else os.getcwd()

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'cookie': '',
    'x-b3-traceid': '',
    'x-s': '',
    'x-t': ''
}
# 读取配置
header_file = SCRIPT_PATH + os.sep + 'xiaohongshu'
if os.path.exists(header_file) is True:
    with open(header_file, encoding='utf-8') as f_header:
        _header = f_header.read()
        _header = json.loads(_header)
        headers.update(_header)

url = 'https://creator.xiaohongshu.com/api/galaxy/creator/week/hotpot'

class xiaohongshuSpider(SpiderApi):

    @classmethod
    def get_hots(cls):
        response = requests.get(url, headers=headers)
        response = response.json()
        items = response.get("data", [])
        hots = []
        rank = 0
        for item in items:
            rank += 1
            link = "https://creator.xiaohongshu.com/topic?topic=%s&page_entrance_type=%s" % (
            item.get("pageId"), item.get("title"))
            _hots = {
                'rank': rank,
                'name': item.get("title"),
                'count': item.get("hotValue"),
                'link': link,
            }
            hots.append(_hots)
        # print(json.dumps(hots,ensure_ascii=False))
        return hots


if __name__ == '__main__':
    xiaohongshuSpider.get_hots()
