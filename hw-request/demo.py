import requests
import logging
import pytest
import json
import os

class TestRequest(object):
    logging.basicConfig(level=logging.INFO)

    url = 'https://testerhome.com/api/v3/topics.json'

    def test_get(self):

        params = {'limit':'2'}
        r = requests.get(self.url,params=params)
        # logging.info(r)
        # logging.info(r.text)

        logging.info(json.dumps(r.json(),indent=2))

    def test_post(self):
        r=requests.post(self.url,
                      headers={'host':'luckycoding.com'},
                      # data={},
                      json={'name':'zitherpeng'},
                      proxies={'https':'127.0.0.1:8888'},
                      verify=False)
        logging.info(r.url)
        logging.info(r.text)


    def test_xueqiu(self):
        query={'_t':'1UNKNOWNc60715cb4a61425b311034a49f4aa024.3446260779.1563002521424.1563005246620',
               '_s':'8c6b2d',
               'category':'1',
               'pid':'-1',
               'size':'10000',
               'x':'1.3',
               'page':'1'}

        r = requests.get('https://101.201.175.228/v5/stock/portfolio/stock/list.json',
                       params=query,
                       headers={'Host':'stock.xueqiu.com',
                                'User-Agent':'Xueqiu Android 11.19'},
                       cookies={'xq_a_token':'5806a70c6bc5d5fb2b00978aeb1895532fffe502',
                                'u':'3446260779'},
                       verify=False,
                       )
        logging.info(json.dumps(r.json(),indent=2))
