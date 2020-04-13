import requests
import time
import random
from lxml import etree

class SearchLinks():
    def __init__(self, url):
        self.header = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
            'Connection': 'keep - alive'
        }
        req = requests.get(url, headers=self.header, timeout=5)
        if req.status_code != 200:
            print('web request is failed.')
        time.sleep(0.5+random.random())
        web_data = self.EncodeData(req=req)
        selector = etree.HTML(web_data)
        # lists = selector.xpath('//td[@style="WORD-WRAP: break-word"]')
        lists = selector.xpath('//a/@href')
        self.link_lists = []
        for list in lists:
            if list[:3] == 'mag' or list[:3] == 'ftp':
                # print(list)
                self.link_lists.append(list)

        # self.link_lists.append(lists.xpath('a/@href'))
        # print(selector.xpath('//a[@target="_self"]'))

    def EncodeData(self, req):
        if req.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(req.text)
            _encoding = None
            if encodings:
                _encoding = encodings[0]
            else:
                _encoding = req.apparent_encoding
        return req.content.decode(_encoding, 'replace')
    
    def Getlinks(self):
        return self.link_lists


if __name__ == '__main__':
    x = SearchLinks(url='https://www.ygdy8.com/html/gndy/dyzz/20191011/59243.html')
    print(x.Getlinks())
