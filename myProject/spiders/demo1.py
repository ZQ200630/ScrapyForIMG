# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import MyprojectItem

class Demo1Spider(scrapy.Spider):
    name = 'demo1'
    allowed_domains = ['unsplash.com']
    # start_urls = ['https://unsplash.com/napi/search/photos?query=picture&xp=&per_page=20&page=2']
    start_urls = ['https://unsplash.com/napi/search/photos?query=picture&xp=&per_page=20&page='+str(i) for i in range(1, 500)]

    def parse(self, response):
        str2 = json.loads(response.text)
        list = str2['results']
        allList = []
        for i in list:
            dic = i['urls']
            allList.append(dic['raw'])
        item = MyprojectItem()
        item['url'] = allList
        yield item
