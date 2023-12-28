# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


#define scrapy items for Cebrennus
class Cebrennus_articles(scrapy.Item):
    Link = scrapy.Field()
    Img_URL = scrapy.Field()
    Title = scrapy.Field()
    Source = scrapy.Field()
    # Description = scrapy.Field()
    Timestamp = scrapy.Field()


#define scrapy items for Hyptiotes
class Hyptiotes_articles(scrapy.Item):
    Link = scrapy.Field()
    Img_URL = scrapy.Field()
    Title = scrapy.Field()
    Source = scrapy.Field()
    Timestamp = scrapy.Field()


#define scrapy items for Galeodes
class Galeodes_articles(scrapy.Item):
    Link = scrapy.Field()
    Img_URL = scrapy.Field()
    Title = scrapy.Field()
    Source = scrapy.Field()
    Timestamp = scrapy.Field()
