# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    info=scrapy.Field()
    num=scrapy.Field()
    location=scrapy.Field()
    pubtime=scrapy.Field()
    link=scrapy.Field()