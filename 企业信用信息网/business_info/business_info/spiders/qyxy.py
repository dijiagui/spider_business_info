# -*- coding: utf-8 -*-
import scrapy
from business_info.items import BusinessInfoItem


class QyxySpider(scrapy.Spider):
    name = "qyxy"
    base_url = 'http://qyxy.baic.gov.cn/'
    allowed_domains = ["qyxy.baic.gov.cn/"]
    start_urls = (
        'http://qyxy.baic.gov.cn/newChange/newChangeAction!gsmd_list.dhtml?clear=true&flag_num=2',
    )

    def parse(self, response):
        page_no = 1
        # 每一个信息块
        item_list = response.xpath("//table[@id='innerTable']")
        for item in item_list:
            url = item.xpath("./tr[1]/td[2]/span/@onclick").extract_first()[13:-23]
            url = self.base_url + url
            yield scrapy.Request(url, callback=self.info_parse, dont_filter=True)
            page_no += 1

        # 获取下一页
        formdata = {
            'SelectPageSize': '50',
            'EntryPageNo': str(page_no-1),
            'pageNo': str(page_no),
            'pageSize': '50'
        }
        post_url = 'http://qyxy.baic.gov.cn/newChange/newChangeAction!gsmd_list.dhtml?clear=true&flag_num=2'
        yield scrapy.FormRequest(post_url, formdata=formdata, callback=self.parse, dont_filter=True)

    def info_parse(self, response):
        """处理出发决定书页面"""
        item = BusinessInfoItem()
        try:
            item['char_num'] = response.xpath("//table//tr")[0].xpath("td[2]/text()").extract()
        except:
            item['char_num'] = 'null'
        try:
            item['company'] = response.xpath("//table//tr")[1].xpath("td[2]/text()").extract()
        except:
            item['company'] = 'null'
        try:
            item['company_id'] = response.xpath("//table//tr")[2].xpath("td[2]/text()").extract()
        except:
            item['company_id'] = 'null'
        try:
            item['legal_person'] = response.xpath("//table//tr")[3].xpath("td[2]/text()").extract()
        except:
            item['legal_person'] = 'null'
        try:
            item['fine_type'] = response.xpath("//table//tr")[4].xpath("td[2]/text()").extract()
        except:
            item['fine_type'] = 'null'
        try:
            item['transact'] = response.xpath("//table//tr")[5].xpath("td[2]/text()").extract()
        except:
            item['transact'] = 'null'
        try:
            item['transact_info'] = response.xpath("//table//tr")[6].xpath("td[2]/text()").extract()
        except:
            item['transact_info'] = 'null'
        try:
            item['transact_time'] = response.xpath("//table//tr")[7].xpath("td[2]/text()").extract()
        except:
            item['transact_time'] = 'null'
        try:
            item['remarks'] = response.xpath("//table//tr")[8].xpath("td[2]/text()").extract()
        except:
            item['remarks'] = 'null'
        yield item




