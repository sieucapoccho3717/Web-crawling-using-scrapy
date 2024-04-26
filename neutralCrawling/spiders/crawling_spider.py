from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class CrawlingSpider(CrawlSpider):
    name = 'crawling_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']


    rules = (
        Rule(LinkExtractor(allow= 'catalogue/category')),
        Rule(LinkExtractor(allow= 'catalogue'), callback='parse_item')
    )



    def parse_item(self, response):
        item = {}
        item['url'] = response.url
        item['title'] = response.xpath('//h1/text()').extract_first()
        item['price'] = response.xpath('//p[@class="price_color"]/text()').extract_first()
        item['availability'] = response.css(".availability::text")[1].get().strip()
        yield item