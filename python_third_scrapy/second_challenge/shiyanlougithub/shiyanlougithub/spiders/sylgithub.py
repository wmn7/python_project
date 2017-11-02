# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem 

class SylgithubSpider(scrapy.Spider):
    name = 'sylgithub'
    
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'

        return (url_tmpl.format(i) for i in range(1, 4))

    def parse(self, response):
        for githubRepositories in response.xpath('//div[@id="user-repositories-list"]/ul/li'):
            item = ShiyanlougithubItem({
                "name": githubRepositories.xpath('.//h3/a/text()').re_first('[^\w]*(\w*)'),
                "update_time": githubRepositories.xpath('.//div/relative-time/@datetime').extract_first()
            })
            yield item
