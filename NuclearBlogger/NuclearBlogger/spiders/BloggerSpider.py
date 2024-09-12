from typing import Any

import scrapy
from scrapy import Selector
from scrapy.http import Response

from NuclearBlogger.items import NuclearbloggerItem
from urllib3.util.url import parse_url


class BloggerSpider(scrapy.Spider):
    name = 'bloggerSpider'

    def __init__(self, **kwargs):
        super(BloggerSpider, self).__init__(**kwargs)
        # "https://hwv430.blogspot.com/search?updated-max=2024-09-12T03:07:00%2B08:00&max-results=50"
        self.start_urls = ["https://hwv430.blogspot.com/"]
        self.num = 0

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: Response, **kwargs: Any):
        blog_list = response.xpath("//div[@class='blog-posts hfeed']/div")
        for blog in blog_list:
            time = blog.xpath("h2[@class='date-header']/span/text()").get()
            posts = blog.xpath("div[@class='date-posts']/div")
            for post in posts:
                blog_item = NuclearbloggerItem()
                blog_item['published_date'] = time
                title = post.xpath("div/h3[@class='post-title entry-title']/a/text()").get()
                # print("title:" + title)
                blog_item['title'] = title
                content = post.xpath("div/div[@class='post-body entry-content']").css("*::text").getall()
                # print("content:" + "\n".join(content))
                blog_item['content'] = ("\n".join(content)).strip()
                yield blog_item

        older_link = response.xpath("//a[@id='Blog1_blog-pager-older-link']")
        if len(older_link) > 0:
            next_url = older_link.xpath('@href').get()
            yield scrapy.Request(next_url, callback=self.parse)
