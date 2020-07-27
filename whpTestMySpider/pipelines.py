# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
logger = logging.getLogger(__name__)

class WhptestmyspiderPipeline(object):
    def process_item(self, item, spider):
        # return item
        # print(item)
        logger.warning("-"*10)
        return item

class WhptestmyspiderPipeline1(object):
    def process_item(self, item, spider):
        # return item
        item["hello"] = "world"
        # print(item)
        return item