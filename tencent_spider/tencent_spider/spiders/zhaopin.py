# -*- coding: utf-8 -*-
import scrapy
from tencent_spider.items import TencentSpiderItem
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class ZhaopinSpider(RedisSpider):
    name = 'zhaopin'
    # allowed_domains = ['tencent.com']
    redis_key = 'zhaopin:start_urls'
    # start_urls = ['http://tencent.com/']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        item=TencentSpiderItem()
        item['name']=response.xpath('//td[@class="l square"]/a/text()').extract()
        item['info']=response.xpath('//tr[@class="even" or @class="odd"]/td[2]/text()').extract()
        item['num'] = response.xpath('//tr[@class="even" or @class="odd"]/td[3]/text()').extract()
        item['location'] = response.xpath('//tr[@class="even" or @class="odd"]/td[4]/text()').extract()
        item['pubtime'] = response.xpath('//tr[@class="even" or @class="odd"]/td[5]/text()').extract()
        item['link'] = response.xpath('//td[@class="l square"]/a/@href').extract()
        yield item

        for i in range(1,239):
            try:
                url='http://hr.tencent.com/position.php?&start='+str(i*10)+'#a'
                print('---这是在爬取第'+str(i)+'页---')
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
                yield Request(url,callback=self.parse,headers=headers)
            except Exception as e:
                print(e)



