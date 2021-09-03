#!/usr/bin/python
# -*- coding: UTF-8 -*-


from spiders.base_spider import *

headers = { 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
url = "https://top.baidu.com/board?tab=realtime"

class BaiduSpider(SpiderApi):

    @classmethod
    def get_hots(cls):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.select('#sanRoot > main > div.container.right-container_2EFJr > div > div:nth-child(2) > div')
        rank = 0
        hots = []
        for item in data:
            rank = rank + 1
            count = item.select('div.trend_2RttY.hide-icon > div.hot-index_1Bl1a')[0].get_text()

            _hots = {
                'rank': rank,
                'name': item.select('div.content_1YWBm > a > div.c-single-text-ellipsis')[0].get_text().strip(),#热、新、沸腾
                'count': count.strip(),
                'link': item.select('div.content_1YWBm > a')[0].get('href'),
            }
            hots.append(_hots)
        # print(json.dumps(hots))
        return hots


if __name__ == '__main__':
    BaiduSpider.get_hots()
