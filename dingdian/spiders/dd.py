# -*- coding: utf-8 -*-
import scrapy
from ..items import DingdianItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DdSpider(CrawlSpider):
    name = 'dd'
    allowed_domains = ['www.booktxt.net']
    start_urls = ['http://www.booktxt.net/1_1666/']

    rules = (
        Rule(LinkExtractor(allow=r'.*\.html', restrict_xpaths='//div[@id="list"]/dl'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = DingdianItem()
        item['title'] = response.xpath('//div[@class="bookname"]/h1/text()').extract_first()
        item['content'] = response.xpath('//div[@id="content"]/text()').extract()
        yield item
