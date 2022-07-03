# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoSpiderItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    motto = scrapy.Field()


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    motto = scrapy.Field()
