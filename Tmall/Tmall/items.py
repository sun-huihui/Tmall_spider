# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmallItem(scrapy.Item):
    # 店铺名字
    shop_name = scrapy.Field()
    # 店铺链接
    shop_link = scrapy.Field()
    # 商品图片
    goods_pic = scrapy.Field()
    # 商品名字
    goods_name = scrapy.Field()
    # 商品价格
    goods_price = scrapy.Field()
    # 商品销量
    goods_salesVolume = scrapy.Field()
    # 商品详情页
    goods_link = scrapy.Field()
    # 爬取时间
    utc_time = scrapy.Field()
    # 数据源
    source = scrapy.Field()
