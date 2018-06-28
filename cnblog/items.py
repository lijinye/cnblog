# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class CnblogItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection='cnblogs'
    title=Field()
    author=Field()
    release_time=Field()
    comments=Field()
    view=Field()
    summary=Field()
    _id=Field()