# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import re

class WifehusbandfilmPipeline(object):
    def process_item(self, item, spider):
        filename = item['title']+'.md'
        item['content'] = item['content'].replace('<div>','').replace('</div>','').replace('<br>','').replace('</span>','').replace('amp;','').replace('<p>','').replace('</p>','').replace('<wbr>','').replace('</wbr>','').replace('<p align="center">','').replace('</strong>','').replace('<strong>','')
        
        #p是用来匹配的
        p = re.compile(r'<a.*?real_src="http://.*?.cn/.*?/(.*?)".*?</a>')
        item['content'] = p.sub(r'\n![](./img/\1.jpg)\n',item['content'])
        
        p = re.compile(r'<a.*?real_src="http://.*?.cn/.*?/(.*?)".*?</a>')
        item['content'] = p.sub(r'\n![](./img/\1.jpg)\n',item['content'])

        p = re.compile(r'<div.*?>')
        item['content'] = p.sub('',item['content'])

        p = re.compile(r'<span.*?>')
        item['content'] = p.sub('',item['content'])

        with open('./film/'+filename,'ab') as fp:
            fp.write(item['title'].encode('utf-8')+b"\n")
            fp.write(item['content'].encode('utf-8')+b"\n")
            fp.write(item['url'].encode('utf-8')+b"\n")
        return item

'''
class MyImagePipelines(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return 'full/%s' % (image_guid)
 
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)
 
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        return item
'''
