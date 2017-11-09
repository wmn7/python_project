# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeiyuluPipeline(object):
    def process_item(self, item, spider):
        fileName = 'weiyulu.txt'
        with open(fileName,'a') as fp:
            fp.write(item['title']+'\n')
            fp.write(item['content']+'\n')
            fp.write(item['url']+'\n\n')
        return item
