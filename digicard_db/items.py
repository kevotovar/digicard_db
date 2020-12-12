# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DigimonCardItem(scrapy.Item):
    name = scrapy.Field()
    number = scrapy.Field()
    cardType = scrapy.Field()
    digimonType = scrapy.Field()
    level = scrapy.Field()
    cardImage = scrapy.Field()
    form = scrapy.Field()
    attribute = scrapy.Field()
    dp = scrapy.Field()
    playCost = scrapy.Field()
    digivolve1Cost = scrapy.Field()
    digivolve2Cost = scrapy.Field()
    effect = scrapy.Field()
    digivoluveEffect = scrapy.Field()
    securityEffect = scrapy.Field()
    rarity = scrapy.Field()
