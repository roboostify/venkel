# -*- coding: utf-8 -*-
import scrapy

from venkel.items import VenkelItem

class ProdPriceSpider(scrapy.Spider):
    """Product price table spider."""
    name = 'prod-price'
    allowed_domains = ['www.venkel.com']
    start_urls = [
        'http://www.venkel.com/',
        ]

    def parse(self, response):
        """Parse all category url."""
        category_urls = response.xpath('//*[@class="home-main-category"]/ul/li/a/@href').extract()

        for url in category_urls:
            yield scrapy.Request(response.urljoin(url),
                                 callback=self.parse_category)

    def parse_category(self, response):
        """Parse every product in each category."""
        product_urls = response.xpath('//div[@class="product-name"]/a/@href').extract()

        for url in product_urls:
            yield scrapy.Request(url, callback=self.parse_product)

        next_page = response.xpath('//a[@title="Next"]/@href').extract_first()
        if next_page:
            yield scrapy.Request(next_page, callback=self.parse_category)

    def parse_product(self, response):
        """Parse product page."""
        mfg_part_id = response.xpath('//tr[descendant::th[text()="Part Number"]]'
                                     '/td/text()').extract_first()
        qty_list = response.xpath('//table[descendant::th[text()="Cut Tape Pricing"]]'
                                  '/tbody[1]/tr[position()>1]/td[position()<=2]/text()').extract()

        item = VenkelItem()
        item['url'] = response.url
        item['site_name'] = 'VENKEL USA'
        item['mfg_part_id'] = mfg_part_id
        item['qty_list'] = qty_list

        yield item
