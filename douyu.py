# -*- coding: utf-8 -*-
import scrapy


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['www.douyu.com']
    start_urls = ['http://www.douyu.com/']

    def parse(self, response):
        pass
