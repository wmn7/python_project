# -*- coding: utf-8 -*-
import scrapy
from shiyanlou_github_repositories.items import ShiyanlouGithubRepositoriesItem

class SylgithubmultSpider(scrapy.Spider):
    name = 'sylgithubmult'
    
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'

        return (url_tmpl.format(i) for i in range(1, 4))

    def parse(self, response):
        for githubRepositories in response.xpath('//div[@id="user-repositories-list"]/ul/li'):
            item = ShiyanlouGithubRepositoriesItem()

            item['name'] = githubRepositories.xpath('.//h3/a/text()').re_first('[^\w]*(\w*)')
            
            item['update_time'] = githubRepositories.xpath('.//div/relative-time/@datetime').extract_first()

            course_url = response.urljoin(githubRepositories.xpath('.//h3/a/@href').extract_first())

            print(course_url)
            print('------------')

            #构造详细页面的请求页
            request = scrapy.Request(course_url,callback=self.parse_r)

            request.meta['item'] = item

            yield request
    
    def parse_r(self,response):
        # 获取未完成的item
        item = response.meta['item']

        item['commits'] = response.xpath('//li[1]/a/span[@class="num text-emphasized"]/text()').re_first('[^\d]*(\d*)[^\d]*')

        item['branches'] = response.xpath('//li[2]/a/span[@class="num text-emphasized"]/text()').re_first('[^\d]*(\d*)[^\d]*')

        item['releases'] = response.xpath('//li[3]/a/span[@class="num text-emphasized"]/text()').re_first('[^\d]*(\d*)[^\d]*')

        yield item
        
