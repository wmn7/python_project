# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from sqlalchemy.orm import sessionmaker
from shiyanlou_github_repositories.models import Repository, engine
from datetime import datetime

class ShiyanlouGithubRepositoriesPipeline(object):

    def process_item(self, item, spider):
        item['update_time'] = datetime.strptime(item['update_time'],'%Y-%m-%dT%H:%M:%SZ')
        item['commits'] = int( item['commits'])
        item['branches'] = int(item['branches'])
        item['releases'] = int(item['releases'])
        self.session.add(Repository(**item))
        return item
        #必须要返回一个item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()