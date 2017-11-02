# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
from sqlalchemy.orm import sessionmaker
from shiyanlou_user.models import User, engine


class ShiyanlouUserPipeline(object):
    def process_item(self, item, spider):
        item['level'] = int(item['level'])
        item['join_date'] = datetime.strptime(item['join_date'], '%Y-%m-%d')
        item['study_record'] = int(item['study_record'])
        self.session.add(User(**item))
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
