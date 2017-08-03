# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import json
from scrapy.exporters import CsvItemExporter


class BusinessInfoPipeline(object):

    def open_spider(self, spider):
        self.redis_cli = redis.StrictRedis(host='127.0.0.1', port=6379)
        # redis.Redis(host = '127.0.0.1', port=6379)

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)
        self.redis_cli.lpush("qyxy_Redis", content)
        return item


class AqiCSVPipeline(object):
    def open_spider(self, spider):
        self.f = open("qyxy.csv", "wb")
        # csv文件读写对象，参数就是csv文件对象
        self.csvexporter = CsvItemExporter(self.f)
        # 开始执行数据写入
        self.csvexporter.start_exporting()

    def process_item(self, item, spider):
        # 将item数据写入到csv文件读写对象对应的文件里
        self.csvexporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 结束数据读写
        self.csvexporter.finish_exporting()
        self.f.close()

