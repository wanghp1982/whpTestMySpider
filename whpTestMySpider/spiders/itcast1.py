# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast1'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # teacher_name = response.xpath('//div[@class="tea_con"]//div[@class="li_txt"]/h3/text()').extract()
        # print(teacher_name)
        li_list = response.xpath('//div[@class="tea_con"]//li')
        for li in li_list:
            item = {}
            # item["teacher_name"] = li.xpath('./h3/text()').extract()[0]
            # item["teacher_title"] = li.xpath('./h4/text()').extract()[0]
            item["teacher_name"] = li.xpath('.//h3/text()').extract_first()
            item["teacher_title"] = li.xpath('.//h4/text()').extract_first()
            item["teacher_desc"] = li.xpath('.//p/text()').extract_first()
            # print(item)
            yield item