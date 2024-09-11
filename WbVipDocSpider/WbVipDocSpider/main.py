import json

from scrapy import cmdline

# cmdline.execute('scrapy crawl WeiboVipDocSpider'.split())

if __name__ == '__main__':
    value = "女性找不到工作别/婚育受歧视吗？"
    print(value.replace('/', '、'))
    print(value)
