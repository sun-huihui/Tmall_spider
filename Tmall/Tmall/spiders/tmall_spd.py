# -*- coding: utf-8 -*-
import json

import math
import scrapy

from items import TmallItem


class TmallSpdSpider(scrapy.Spider):
    name = 'tmall_spd'
    allowed_domains = ['tmall.com']
    nextpage_url = "https://list.tmall.com/search_product.htm"
    goods_base = "/shop/shop_auction_search.do"
    start_urls = ['https://tmall.com/']
    num = 2

    def parse(self, response):
        a_link = response.xpath('//li[@data-spm="category2016013"]//a[1]/@href').extract()[0]
        a_url = "https:" + a_link
        print "[INFO]:发送美妆分类请求...."
        print a_url
        yield scrapy.Request(a_url, callback=self.parse_shop, dont_filter=True)
        print "[INFO]:发送...."

    def parse_shop(self, response):

        print "[INFO]:获取店铺链接...."
        shop_link = response.xpath('//div[@class="shopHeader-enter"]/a[1]/@href')
        for link in shop_link:
            url = "https:" + link.extract()
            yield scrapy.Request(url, callback=self.parse_goods, dont_filter=True)

        next_page = response.xpath('//a[@class="ui-page-next"]/@href').extract()
        if next_page:
            print "[INFO]:第%d页，下一页url..."%self.num, len(next_page)
            yield scrapy.Request(self.nextpage_url + next_page[0], callback=self.parse_shop, dont_filter=True)
            self.num += 1

    def parse_goods(self, response):
        print "[INFO]:获取店内全部商品列表链接..."
        link = response.xpath('//a[@class="slogo-shopname"]/@href').extract()[0]
        shop_link = "https:" + link.split('?')[0]
        goods_url = "m.tmall".join(shop_link.split('tmall')) + self.goods_base
        yield scrapy.Request(goods_url, callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        data = json.loads(response.body)
        shopurl = "https:" + data['shop_Url']
        shop_name = data["shop_title"]
        total = int(data["total_page"])
        goods_data = data["items"]
        now_page = int(data['current_page'])

        print "-" * 30
        print shop_name[:4], '[INFO]:正在爬取第%d的数据。。。'%now_page
        print "-" * 30

        for the_item in goods_data:
            item = TmallItem()
            item['shop_name'] = shop_name
            item['shop_link'] = shopurl
            item["goods_pic"] = "https:" + the_item['img']
            item["goods_name"] = the_item['title']
            try:
                item["goods_price"] = the_item['price']
            except:
                item["goods_price"] = "None"
            item["goods_salesVolume"] = the_item['sold']
            item["goods_link"] = "https:" + the_item['url']
            yield item

        print "-" * 30
        print "共%d页"%total
        print '[INFO]:第%d的数据完成。。。' % now_page
        print "-" * 30

        if now_page < total:
            print "now_page", now_page
            now_page += 1
            url = "m.tmall".join(shopurl.split("tmall")) + self.goods_base + "?p=" + str(now_page)
            yield scrapy.Request(url, callback=self.parse_detail, dont_filter=True)





