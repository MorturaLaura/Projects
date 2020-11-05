import os
import scrapy
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
from items import WebscrapyItem


class ImobiliareSpider(scrapy.Spider):
    name = 'imobiliare'
    # allowed_domains = ['https://www.imobiliare.ro/inchirieri-apartamente/cluj-napoca']

    start_urls = ['https://www.imobiliare.ro/inchirieri-apartamente/cluj-napoca?pagina=1']

    try:
        os.remove('rent_price_results.csv')
    except OSError:
        pass

    def start_request(self):
        yield scrapy.Request('https://www.imobiliare.ro/inchirieri-apartamente/cluj-napoca?pagina=1', callback=self.parse)

    def parse(self, response):
        all_ads = response.xpath('//div[@class="box-anunt"]')
        for ads in all_ads:
            loader = ItemLoader(item=WebscrapyItem(), selector=ads, response=response)
            loader.add_xpath("neighborhood", ".//div[@class='localizare']/p/text()")
            loader.add_xpath("price", ".//span[@class='pret-mare']/text()")
            loader.add_xpath("currency", ".//span[@class='tva-luna']/text()")
            loader.add_xpath("rooms", ".//ul[@class='caracteristici']/li[1]/span/text()")
            loader.add_xpath("space", ".//ul[@class='caracteristici']/li[2]/span/text()")
            loader.add_xpath("floor", ".//ul[@class='caracteristici']/li[3]/span/text()")
            loader.add_xpath("partitioning", ".//ul[@class='caracteristici']/li[4]/span/text()")
            loader.add_xpath("new_building", ".//ul[@class='caracteristici']/li[5]/span/text()")
            yield loader.load_item()

        next_page = response.xpath("//a[@class='inainte butonpaginare']/@href").get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)


if __name__ == "__main__":
    # create Instance called 'imob' as in imobilare
    imob = CrawlerProcess(settings={
        "FEEDS": {
            "rent_price_results.csv": {"format": "csv"},
            },
            })

    imob.crawl(ImobiliareSpider)
    imob.start()
