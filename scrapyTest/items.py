# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    游戏地址 = scrapy.Field()
    游戏图片 = scrapy.Field()
    游戏名字 = scrapy.Field()
    游戏类型 = scrapy.Field()
    pass
