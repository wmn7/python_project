#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShiyanlouUserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    join_date = scrapy.Field()
    level = scrapy.Field()
    status = scrapy.Field()
    school = scrapy.Field()
    job = scrapy.Field()
    study_record = scrapy.Field()
