#! /Library/Framework/Python.framework/Versions/2.7/bin/python2.7
# -*- coding: utf-8 -*-
from scrapy import cmdline


def main():
    cmdline.execute("scrapy crawl tmall_spd".split())


if __name__ == "__main__":
    main()
