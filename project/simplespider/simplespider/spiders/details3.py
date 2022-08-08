import scrapy
from simplespider.items import DetailItem

class ItemData(scrapy.Spider):
    name = 'itemdata'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/trending-tickers']
    def parse(self,response):
        # XPaths
        xpath_a = '//*[@id="list-res-table"]/div[1]/table/tbody/tr/td[1]/a/text()'
        xpath_b = '//*[@id="list-res-table"]/div[1]/table/tbody/tr/td[2]/text()'
        xpath_c = '//*[@id="list-res-table"]/div[1]/table/tbody/tr/td[3]/fin-streamer/text()'
        xpath_d = '//*[@id="list-res-table"]/div[1]/table/tbody/tr/td[1]/a/@href'
        # XPath parse assignment
        company_symbol = response.xpath(xpath_a).extract()
        company_name = response.xpath(xpath_b).extract()
        company_price = response.xpath(xpath_c).extract()
        company_link = response.xpath(xpath_d).extract()
        # DetailItem instance 
        details_item = DetailItem()
        # Loop assignment
        for symbol, name, price, link in zip(company_symbol, company_name, company_price, company_link):
            details_item['company_symbol'] = symbol
            details_item['company_name'] = name
            details_item['company_price'] = price
            details_item['company_link'] = 'https://finance.yahoo.com/trending-tickers' + link
            yield details_item