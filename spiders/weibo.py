#!/usr/bin/python
# -*- coding: UTF-8 -*-


from spiders.base_spider import *

headers = { 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}


class WeiboSpider(SpiderApi):

    @classmethod
    def get_hots(cls):
        url = 'https://s.weibo.com/top/summary/summary?cate=realtimehot'
        response = requests.get(url, headers=headers)
        # print(response.text)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.select('.hotrank >section.list> ul.list_a > li')
        # print(data)
        hots = []
        for item in data:
            rank_strong = item.select("a > strong.hot ")
            # print(rank_strong)
            if rank_strong is None or len(rank_strong)==0:
                continue
            hotCount = item.select("a > span > em ")[0].get_text()
            rank = rank_strong[0].get_text()
            name = item.select("a > span ")[0].decode()
            name = re.sub(r'<em>\d+</em>', "", name)
            name = filter_tags(name)
            _hots = {
                'rank': rank,
                'name': name,
                'count': hotCount,
                'link': 'https://s.weibo.com/' + item.select("a")[0].get('href'),
            }
            hots.append(_hots)
        # print(json.dumps(hots))
        return hots

    @classmethod
    def get_hots_topics(cls):
        url = 'https://s.weibo.com/top/summary/summary?cate=topicband'
        response = requests.get(url, headers=headers)
        # print(response.text)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.select('.hotrank >section.list> ul.list_b > li')
        # print(data)
        hots = []
        for item in data:
            rank_strong = item.select("a > div > em ")
            # print(rank_strong)
            if rank_strong is None or len(rank_strong) == 0:
                continue
            hotCount = item.select("a > article > span ")[0].get_text()
            rank = rank_strong[0].get_text()
            name = item.select("a > article > h2 ")[0].get_text()
            name = filter_tags(name)
            desc = item.select("a > article > p ")[0].get_text()
            _hots = {
                'rank': rank,
                'name': name,
                'count': hotCount,
                'link': 'https://s.weibo.com' + item.select("a")[0].get('href'),
                'desc': desc,
            }
            hots.append(_hots)
        # print(json.dumps(hots))
        return hots

if __name__ == '__main__':
    # WeiboSpider.get_hots()
    WeiboSpider.get_hots_topics()