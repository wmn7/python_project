# -*- coding: utf-8 -*-
import scrapy
from weiyulu.items import WeiyuluItem

class WeiyuluspiderSpider(scrapy.Spider):
    
    name = 'weiyuluSpider'
    
    start_urls = ['http://www.weiyulu.cn/shenghuoganwu/2254.html']


    def parse(self, response):
        
        item = WeiyuluItem()
        item['url'] = response.xpath('//h1/a/@href').extract_first()
        item['title'] = response.xpath('//h1/a/text()').extract_first()
        item['content'] = response.xpath('//div[@class="single-content"]/p/text()').extract_first()
        yield item

        print('--------------')
        newUrl = response.xpath('//nav/a[@rel="next"]/@href').extract_first()
        yield response.follow(newUrl,callback=self.parse)

