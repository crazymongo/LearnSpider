import json
import os.path
from typing import Any

import scrapy
from scrapy.http import Request, Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from ..items import WbVipDocSpiderItem


class WeiboVipDocSpiderV2(scrapy.Spider):
    name = 'WeiboVipDocSpiderV2'

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        # complete_set = list()
        # with open("complete_set.txt", "r") as f:
        #     while line := f.readline():
        #         complete_set.append(line.strip())
        #     f.close()

        # self.start_urls = list()
        # with open("contentlist_test.json", "r") as f:
        #     json_data = json.load(f)
        #     json_data_list = json_data.get("data").get("list")
        #
        #     for item in json_data_list:
        #         if item.get("type") == 1:
        #             url = item.get("url")
        #             if url not in complete_set:
        #                 self.start_urls.append(url)
        #     f.close()
        self.start_urls = ['https://card.weibo.com/article/m/show/id/2309404315413180739586?_wb_client_=1']
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('no=sandbox')
        self.option.add_argument('--blink-setting=imagesEnable=true')
        self.driver = webdriver.Chrome(self.option)
        self.driver.set_page_load_timeout(30)

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response: Response, **kwargs: Any):
        self.driver.get(response.url)
        with open("cookies.txt", 'r') as f:
            cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            f.close()
        self.driver.refresh()
        # self.driver.get(response.url)
        try:
            title = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, "f-art-tit")))
            # title = self.driver.find_element(by=By.CLASS_NAME, value="f-art-tit")
            print("title: " + title.text)
            print("url: " + response.url)
            content = self.driver.find_element(by=By.CLASS_NAME, value='art-con-new')
            print(content.text)
            # item = WbVipDocSpiderItem()
            # item['title'] = title
            # item['content'] = content
            # item['url'] = response.url
            # yield item
        except Exception as e:
            print(e)
            # error_msg = self.driver.find_element(by=By.CLASS_NAME, value='error_msg')
            # print(error_msg.text)
            # item = WbVipDocSpiderItem()
            # item['content'] = None
            # if error_msg is not None:
            #     item['error_msg'] = error_msg.text
            # else:
            #     item['error_msg'] = "unknown error"
            # item['url'] = response.url
            # yield item
