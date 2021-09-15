#!/usr/bin/python
# -*- coding: UTF-8 -*-


from spiders.base_spider import *

headers = { 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
url = 'https://tophub.today/n/K7GdaMgdQy'

class DouyinSpider(SpiderApi):

    @classmethod
    def get_hots(cls):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.select( '#page > div.c-d.c-d-e > div.Zd-p-Sc > div:nth-child(1) > div.cc-dc-c > div > div.jc-c > table > tbody > tr')
        hots = []
        for item in data:
            rank = item.select('td')[0].get_text()
            rank = rank.strip(".")
            name = item.select('tr > td.al > a')[0].get_text()
            _hots = {
                'rank': rank,
                'name': name,
                'count': item.select('td')[2].get_text(),
                'link': "https://www.douyin.com/search/"+name+"?source=normal_search&enter_from=recommend" ,
            }
            hots.append(_hots)
        # print(json.dumps(hots))
        return hots


if __name__ == '__main__':
    DouyinSpider.get_hots()