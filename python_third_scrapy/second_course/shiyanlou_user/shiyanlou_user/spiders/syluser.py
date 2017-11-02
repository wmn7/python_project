# -*- coding: utf-8 -*-
import scrapy
from shiyanlou_user.items import ShiyanlouUserItem

class SyluserSpider(scrapy.Spider):
    name = 'syluser'
    
    @property
    def start_urls(self):
        url_tmpl = 'https://www.shiyanlou.com/user/{}/'
        return (url_tmpl.format(i) for i in range(200, 1,-10))

    def parse(self, response):
        yield ShiyanlouUserItem({
        'name':response.xpath('//div[@class="userinfo-banner-meta"]/span[@class="username"]/text()').extract_first(),
        'type':response.xpath('//a[@class="member-icon"]/img[@class="user-icon"]/@title').extract_first(default='普通用户'),
        'join_date':response.xpath('//span[@class="join-date"]/text()').re_first('((\d|-)*)[^\d]*'),
        'level':response.xpath('//span[@class="user-level"]/text()').re_first('[^\d]*(\d*)'),
        'status':response.xpath('//div[@class="userinfo-banner-status"]/span/text()').extract_first(),
        'job': response.xpath('//div[@class="userinfo-banner-status"]/span[2]/text()').extract_first(),
        'school': response.xpath('//div[@class="userinfo-banner-status"]/a/text()').extract_first(),
        'study_record':response.xpath('//span[@class="latest-learn-num"]/text()').extract_first()
        })

