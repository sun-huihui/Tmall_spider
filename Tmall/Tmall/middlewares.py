# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import random
from settings import USER_AGENT_LIST


class UserAgentMiddleware(object):

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers.setdefault("User-Agent", user_agent)


class ProxyMiddlewares(object):
    def process_request(self, request, spider):
        # 免费代理的使用（写前两行）
        # proxy = "mr_mao_hacker:sffqry9r@116.62.128.50:16816"
        proxy = "116.62.128.50:16816"
        request.meta["proxy"] = "http://" + proxy

        # 验证代理的账户名和密码
        user_passwd = "mr_mao_hacker:sffqry9r"
        # 将账户名和密码经过base64编码处理
        base64_user_passwd = base64.b64encode(user_passwd)
        request.headers["Proxy-Authorization"] = "Basic " + base64_user_passwd
