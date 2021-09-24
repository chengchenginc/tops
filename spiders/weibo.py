#!/usr/bin/python
# -*- coding: UTF-8 -*-


from spiders.base_spider import *

headers = { 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36',
'Cookie': 'SINAGLOBAL=2233539411227.5654.1601454376571; SCF=AlBKGORvaJsW8-nEmzFtt7dqwZnQhVAJ4JuR_biCMn8OXymuaOlm_9dsOr9MlYzeKBWYBBiEHQ5rF9RFfcvZ3MA.; UOR=www.baidu.com,vdisk.weibo.com,chengchenginc.github.io; SUB=_2AkMWEaR0f8NxqwJRmPATyGLjaIh0yA_EieKgTVWvJRMxHRl-yT92qnYgtRB6PZGKm3Mkunxhyoqk84H4tRmcQVcSxAEA; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFvMs4cFrcyXicI0MMMviov; _s_tentry=passport.weibo.com; Apache=6350920181265.767.1632447305265; ULV=1632447305349:21:9:2:6350920181265.767.1632447305265:1632295091864; WBStorage=d335429e|undefined'
            }


class WeiboSpider(SpiderApi):

    @classmethod
    def get_hots(cls):
        url = 'https://s.weibo.com/top/summary?cate=realtimehot'
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
        url = 'https://s.weibo.com/top/summary?cate=topicband'
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