#!/usr/bin/python
# -*- coding: UTF-8 -*-


from spiders.base_spider import *

headers = {
    'Referer': "https://www.zhihu.com/billboard",
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}
url = 'https://www.zhihu.com/billboard'

class ZhihuSpider(SpiderApi):

    @classmethod
    def get_hots(cls):
        response = requests.get(url, headers=headers)
        html = response.text
        content = re.findall(r'<div class="HotList-itemTitle">([\s\S]+?)</div>', html, re.M)
        hot = re.findall(r'<div class="HotList-itemMetrics">([\s\S]+?)</div>', html, re.M)
        urls = re.findall(r'"link":{"url":"([\s\S]+?)"}},', html, re.M)
        describe = re.findall(r'"excerptArea":{"text":"([\s\S]+?)"},', html, re.M)
        hots = []
        rank = 0
        for i in range(len(content)):
            rank = rank + 1
            _hots = {
                'rank': rank,
                'name': content[i],
                'count':  hot[i],
                'link': str(urls[i]).replace('u002F', ''),
                'desc': describe[i]
            }
            hots.append(_hots)
        # print(json.dumps(hots))
        return hots


if __name__ == '__main__':
    ZhihuSpider.get_hots()
