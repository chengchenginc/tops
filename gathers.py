#!/usr/bin/python
# -*- coding: UTF-8 -*-

from conf.settings import *
from spiders.baidu import *
from spiders.douyin import *
from spiders.toutiao import *
from spiders.weibo import *
from spiders.zhihu import *


def gather_data():
    now = time.time()
    _datetime = datetime.datetime.fromtimestamp(int(now)).strftime("%Y年%m月%d日 %H:%M:%S")
    # baidu
    baidu_hots = BaiduSpider.get_hots()
    print("baidu over")
    # douyin
    douyin_hots = DouyinSpider.get_hots()
    print("douyin over")
    # toutiao
    toutiao_hots = ToutiaoSpider.get_hots()
    print("toutiao over")
    # weibo
    weibo_hots = WeiboSpider.get_hots()
    weibo_hots_topics = WeiboSpider.get_hots_topics()
    print("weibo over")
    # zhihu
    zhihu_hots = ZhihuSpider.get_hots()
    print("zhihu over")
    all_hots = {
        'baidu': {"tops": baidu_hots, "name": "百度热搜"},
        'douyin': {"tops": douyin_hots, "name": "抖音热搜"},
        'toutiao': {"tops": toutiao_hots, "name": "头条热搜"},
        'weibo_search': {"tops": weibo_hots, "name": "微博热搜"},
        'weibo_topic': {"tops": weibo_hots_topics, "name": "微博话题"},
        'zhihu': {"tops": zhihu_hots, "name": "知乎热搜"}
    }

    _date = datetime.datetime.fromtimestamp(int(now)).strftime("%Y%m%d")
    ##处理今日实时点评数据
    date_file_path = DATA_PATH + _date + "_hots.json"
    index_file_path = DATA_PATH + "index_hots.json"
    json_data = {"tops": all_hots, "datetime": _datetime}
    content = json.dumps(json_data, ensure_ascii = False)
    with open(date_file_path, mode="w", encoding="utf-8") as f1:
        f1.write(content)
    with open(index_file_path, mode="w", encoding="utf-8") as f2:
        f2.write(content)


if __name__ == '__main__':
    # weibo_hots = WeiboSpider.get_hots()
    gather_data()
