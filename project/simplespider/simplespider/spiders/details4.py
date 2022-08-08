import scrapy
from simplespider.items import DetailLoader
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class ItemData(scrapy.Spider):
    name = 'detailloadersio'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/trending-tickers']
    def parse(self,response):
        # XPaths
        xpath_a = '//*[@id="list-res-table"]/div[1]/table/tbody/tr'
        # XPath parse assignment
        stock_info = response.xpath(xpath_a)
        # Loop assignment
        for info in stock_info:
            detail_loader = ItemLoader(item = DetailLoader(), selector = info)
            detail_loader.default_output_processor = TakeFirst()
            detail_loader.add_xpath('company_symbol', 'td[1]/a/text()')
            detail_loader.add_xpath('company_name', 'td[2]/text()')
            detail_loader.add_xpath('company_price', 'td[3]/fin-streamer/text()')
            detail_loader.add_xpath('company_link', 'td[1]/a/@href')
            yield detail_loader.load_item()

