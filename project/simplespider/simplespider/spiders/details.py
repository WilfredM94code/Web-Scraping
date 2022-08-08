import scrapy


class DetailsSpider(scrapy.Spider):
    name = 'details'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/trending-tickers']
    
    def parse(self, response):
        xpath_a = '//*[@id="list-res-table"]/div[1]/table/tbody/tr/td[2]/text()'
        xpath_b = '//*[@id="list-res-table"]/div[1]/table/tbody/tr/td[3]/fin-streamer/text()'
        company_name_list = response.xpath(xpath_a).extract()
        company_price_list = response.xpath(xpath_b).extract()
        for name,price in zip(company_name_list,company_price_list):
            print (f'{name} - {price}')
