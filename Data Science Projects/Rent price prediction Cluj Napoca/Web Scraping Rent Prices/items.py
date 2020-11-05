# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from itemloaders.processors import TakeFirst
from scrapy.loader.processors import MapCompose

import scrapy


def remove_n(value):
    return value.replace("\n", '')


class WebscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    neighborhood = scrapy.Field(
        input_processor=MapCompose(str.strip, remove_n),
        output_processor=TakeFirst()
    )
    price = scrapy.Field()
    currency = scrapy.Field()
    rooms = scrapy.Field()
    space = scrapy.Field()
    floor = scrapy.Field()
    partitioning = scrapy.Field()
    new_building = scrapy.Field()
