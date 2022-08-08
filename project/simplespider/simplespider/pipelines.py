class FilterData100(object):
    def process_item (self, item, spider):
        try:
            price = float (item['company_price'])
            if price > 100:
                item['company_price'] = '>100'
        except:
            pass
        return item

class FilterData50(object):
    def process_item (self, item, spider):
        try:
            price = float (item['company_price'])
            if price < 50:
                item['company_price'] = '<50'
        except:
            pass
        return item