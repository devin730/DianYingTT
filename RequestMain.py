#!/usr/bin/python
#coding: utf-8

import requests
import time
import random
from lxml import etree
import xlwt
from MovieHeaven import SunshineMovie
from MPage import SearchLinks

class MainMovie():
    def __init__(self, url, save_filename):
        self.header = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
            'Connection': 'keep - alive'
        }
        self.url_start = url  # "https://www.dytt8.net/html/gndy/jddy/20160320/50523.html"
        self.file_name = save_filename
        self.movie_name = ''
        self.movie_down_links = []
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.worksheet = self.workbook.add_sheet('高分电影资源下载整理')

        # 设置Excel的样式
        # 设置统一的字体
        font = xlwt.Font()
        font.name = 'Time New Roman'
        font.size = 14

        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER

        self.common_style = xlwt.XFStyle()
        self.common_style.font = font

        # col 0 2 3 水平居中，其余不变
        self.style023 = xlwt.XFStyle()
        self.style023.font = font
        self.style023.alignment = alignment

        # 设置列宽
        self.worksheet.col(0).width = 256 * 20  # 256是度量单位，20表示20个字符的宽度
        self.worksheet.col(1).width = 256 * 200
        self.worksheet.col(2).width = 256 * 200
        # self.worksheet.col(3).width = 256 * 8
        # self.worksheet.col(4).width = 256 * 20
        # self.worksheet.col(5).width = 256 * 20
        # self.worksheet.col(6).width = 256 * 20
        # self.worksheet.col(7).width = 256 * 20
        # self.worksheet.col(8).width = 256 * 20
        # self.worksheet.col(9).width = 256 * 30
        # self.worksheet.col(10).width = 256 * 100

        # 设置标题栏
        self.worksheet.write(0, 0, label='电影名称', style=self.style023)
        self.worksheet.write(0, 1, label='下载链接1', style=self.common_style)
        self.worksheet.write(0, 2, label='下载链接2', style=self.style023)

        self.write_line = 0
        # self.worksheet.write(0, 3, label='年份', style=self.style023)
        # self.worksheet.write(0, 4, label='导演', style=self.common_style)
        # self.worksheet.write(0, 5, label='明星', style=self.common_style)
        # self.worksheet.write(0, 6, label='国家', style=self.common_style)
        # self.worksheet.write(0, 7, label='类型', style=self.common_style)
        # self.worksheet.write(0, 8, label='评论数', style=self.common_style)
        # self.worksheet.write(0, 9, label='短评', style=self.common_style)
        # self.worksheet.write(0, 10, label='网址', style=self.common_style)
        self.BeginCrawl(self.url_start)
        self.workbook.save(self.file_name)

    def EncodeData(self, req):
        if req.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(req.text)
            _encoding = None
            if encodings:
                _encoding = encodings[0]
            else:
                _encoding = req.apparent_encoding
        return req.content.decode(_encoding, 'replace')

    def BeginCrawl(self, url):
        req = requests.get(url, headers=self.header, timeout=5)
        if req.status_code != 200:
            print('web request is failed.')
        web_data = self.EncodeData(req=req)
        # print(web_data)
        selector = etree.HTML(web_data)
        
        lists = selector.xpath('//font[@color="#ff0000"]/p')
        for list in lists:
            print('___START___')
            if len(list.xpath('text()')) == 0:
                print('___END___')
                continue
            print(list.xpath('text()'))
            self.movie_name = self.GetMovieName(list.xpath('text()')[0])
            if self.movie_name is None:
                print('无效条目')
                print('___END___')
                continue
            else:
                print(self.movie_name)
            
            if len(list.xpath('a/@href')) == 0:

                in_params = {"typeid": "1", "keyword": ""}
                try:
                    in_params['keyword'] = self.movie_name.encode('gb2312')
                except Exception:
                    continue
                s = SunshineMovie()
                print('特殊情况, 直接搜条目')
                for item in s.get_display_content(params=in_params):
                    self.movie_down_links.append(item)
                print(self.movie_down_links)
            else:
                lks = SearchLinks(list.xpath('a/@href')[0])
                self.movie_down_links.extend(lks.Getlinks())
            print('___END___')

            self.WriteToExcel()
            # time.sleep(random.random() + 1)
    
    def GetMovieName(self, label):
        start = label.find('《')
        end = label.find('》')
        if start == -1 or end == -1:
            return None
        else:
            name = label[start+1:end]
            return name
    
    def WriteToExcel(self):
        self.write_line = self.write_line + 1
        self.worksheet.write(self.write_line, 0, label=self.movie_name, style=self.style023)
        if len(self.movie_down_links) < 1:
            return
        self.worksheet.write(self.write_line, 1, label=self.movie_down_links[0], style=self.common_style)
        if len(self.movie_down_links) < 2:
            return
        self.worksheet.write(self.write_line, 2, label=self.movie_down_links[1], style=self.common_style)
        self.movie_name = ''
        self.movie_down_links = []
        self.workbook.save(self.file_name)

    
if __name__ == '__main__':
    MainMovie(url="https://www.dytt8.net/html/gndy/jddy/20160320/50523.html", save_filename='excel1.xls')
