# -*- coding: utf-8 -*-
import scrapy
from wifehusbandfilm.items import WifehusbandfilmItem
import requests
import time
import re

class WifehfilmSpider(scrapy.Spider):
    name = 'wifehFilm'

    @property
    def start_urls(self):
        url_tmpl = 'http://blog.sina.com.cn/s/articlelist_1377336233_2_{}.html/'
        return (url_tmpl.format(i) for i in range(1,9))

    def parse(self, response):
        for filmurl in response.xpath('//div[@class="articleList"]/div/p/span[@class="atc_title"]/a/@href').extract():
            item = WifehusbandfilmItem()
            #找到文章的链接
            item['url'] = filmurl
            request = scrapy.Request(filmurl,callback=self.parse_film)
            request.meta['item'] = item
            yield request

    def parse_film(self,response):
        print('ok')
        #获取未完成的item
        item = response.meta['item']
        #获取电影标题        
        item['title'] = response.xpath('//div[@class="articalTitle"]/h2/text()').re_first('[【夫妻影评】]*(.*)')
        print(item['title'])
        #获取文章内容
        item['content'] = response.xpath('//div[@id="sina_keyword_ad_area2"]').extract_first()
        #获取图片的url
        item['image_urls'] = response.xpath('//div[@id="sina_keyword_ad_area2"]/div/a/img/@real_src').extract()
        
        if item['image_urls']==[]:
            item['image_urls'] = response.xpath('//div[@id="sina_keyword_ad_area2"]/p/a/img/@real_src').extract()
        
        for image_url in item['image_urls']:
            
            p = re.compile(r'http://.*?.cn/.*/(.*)')
            image_name = p.sub(r'./film/img/\1.jpg',image_url)
            self.download_image(image_url,image_name)

        yield item

    def download_image(self,imageurl,imagename):  
        p = True
        i = 0

        print(imageurl)
        print('--------------')
        while p and i<=2:  
            try:  
                data=requests.get(imageurl,timeout=20).content  
                with open(imagename,'wb') as f:  
                    f.write(data)  
                p=False  
            except:  
                i+=1  
                print('save picture wrong,please wait 2 seconds')  
                time.sleep(2)  



        
