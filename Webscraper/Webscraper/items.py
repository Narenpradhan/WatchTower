# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Cebrennus_articles(scrapy.Item):
    Link = scrapy.Field()
    Title = scrapy.Field()
    # Description = scrapy.Field()
    Timestamp = scrapy.Field()


class Hyptiotes_articles(scrapy.Item):
    Link = scrapy.Field()
    Title = scrapy.Field()
    Timestamp = scrapy.Field()


class Galeodes_articles(scrapy.Item):
    Link = scrapy.Field()
    Title = scrapy.Field()
    Timestamp = scrapy.Field()
