# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BusinessInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name= scrapy.Field()
    char_num = scrapy.Field()  # 行政处罚决定书文号
    company = scrapy.Field()  # 当事人名称
    company_id = scrapy.Field()  # 当事人注册号
    legal_person = scrapy.Field()  # 法定代表人（负责人）
    fine_type = scrapy.Field()  # 违法行为类型
    transact = scrapy.Field()  # 行政处罚决定机关名称
    transact_info = scrapy.Field()  # 行政处罚内容
    transact_time = scrapy.Field()  # 作出行政处罚决定日期
    remarks = scrapy.Field()  # 备注



