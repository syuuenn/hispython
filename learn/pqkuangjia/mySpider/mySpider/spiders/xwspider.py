# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mySpider.items import MyspiderItem

class XwspiderSpider(CrawlSpider):
    name = 'xwspider'
    allowed_domains = ['news.baidu.com']
    start_urls = ['http://news.baidu.com']

    rules = (
        Rule(LinkExtractor(allow=r'http://news.baidu.com/tech'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print('###################################')
        node_list_name = response.xpath('//div[@id="col_focus"]/div/div/ul/li/a/text()')
        node_list_url=response.xpath('//div[@id="col_focus"]/div/div/ul/li/a/@href')
        for i in range(0,len(node_list_name)):
            item=MyspiderItem()

            xwname=node_list_name[i].extract()
            xwurl=node_list_url[i].extract()
            item['xwname']=xwname
            # print(xwname)
            # print(xwurl)
            yield scrapy.Request(url=xwurl,callback=self.nx_handler,meta={'item':item},dont_filter=True)

        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
    def nx_handler(self,response):

        item = response.meta['item']
        img_urls = response.xpath('//div[@id="article"]//img/@src')
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print(len(img_urls))
        zburl=[]
        for obj in img_urls:
            zburl.append(obj.extract())
        item['imgurl'] = zburl

        yield item

