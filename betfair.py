import scrapy
from scrapy.pipelines.files import FilesPipeline


file_filter = ['dwbfpricesirewin', 'dwbfpricesukwin']
base_url = 'https://promo.betfair.com'


class CsvItem(scrapy.Item):
    file_urls = scrapy.Field()


class CustomFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        file_name = request.url.split('/')[-1]
        return file_name


class BetfairSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://promo.betfair.com/betfairsp/prices',
    ]
    custom_settings = {
        'ITEM_PIPELINES': {__name__ + '.CustomFilesPipeline': 1},
        'FILES_STORE': './downloads/',
        'MEDIA_ALLOW_REDIRECTS': True
    }

    def parse(self, response):
        for link in response.css('a[href*=csv]::attr(href)'):
            link = link.get()
            if any(filter in link for filter in file_filter):
                link_url = base_url + link
                yield CsvItem(file_urls=[link_url])