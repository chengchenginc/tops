#!/usr/bin/python
# -*- coding: UTF-8 -*-


from spiders.base_spider import *
import json
import base64

headers = {
    'Referer': "https://www.zhihu.com/billboard",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
url = 'https://www.zhihu.com/billboard'

class ZhihuSpider(SpiderApi):

    @classmethod
    def get_hots(cls):
        response = requests.get(url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        data = soup.select('#js-initialData')[0].get_text()
        data = json.loads(data)

        hots_data = data.get("initialState",{}).get("topstory",{}).get("hotList",[])
        hots = []
        rank = 0
        for i in range(len(hots_data)):
            rank = rank + 1
            _hots = {
                'rank': rank,
                'name': hots_data[i].get("target",{}).get("titleArea",{}).get("text",""),
                'count':  hots_data[i].get("target",{}).get("metricsArea",{}).get("text",""),
                'link': hots_data[i].get("target",{}).get("link",{}).get("url",""),
                'desc': hots_data[i].get("target",{}).get("excerptArea",{}).get("text",""),
            }
            hots.append(_hots)
        # print(json.dumps(hots))
        return hots


if __name__ == '__main__':
    ZhihuSpider.get_hots()
