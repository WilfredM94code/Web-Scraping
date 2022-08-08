# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DetailItem(scrapy.Item):
    company_symbol = scrapy.Field()
    company_name = scrapy.Field()
    company_price = scrapy.Field()
    company_link = scrapy.Field()


# Item Loaders & Input and Output Processors
from scrapy.loader.processors import MapCompose

def full_links(company_symbol_link):
    url = 'https://finance.yahoo.com/trending-tickers'
    return url + company_symbol_link

class DetailLoader(scrapy.Item):
    company_symbol = scrapy.Field()
    company_name = scrapy.Field()
    company_price = scrapy.Field()
    company_link = scrapy.Field(input_processor = MapCompose(full_links))