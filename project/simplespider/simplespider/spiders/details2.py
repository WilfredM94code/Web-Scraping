import scrapy
from datetime import datetime


file_name = f'stock_detail_at_{str(datetime.timestamp(datetime.now()))}.txt'

class CurrentCompanyData(scrapy.Spider):
    name = 'currentdata'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/trending-tickers']
    def parse(self,response):
        xpath_a = '//*[@id="list-res-table"]/div[1]/table/tbody/tr/td[2]/text()'
        xpath_b = '//*[@id="list-res-table"]/div[1]/table/tbody/tr/td[3]/fin-streamer/text()'
        company_name_list = response.xpath(xpath_a).extract()
        company_price_list = response.xpath(xpath_b).extract()
        with open (file_name, '+a') as file:
            file.write (f'//\n{str(datetime.timestamp(datetime.now()))}\n')
            for name,price in zip(company_name_list,company_price_list):
                file.write (f'{name} - {price}\n')
            file.write ('\\\\\n')