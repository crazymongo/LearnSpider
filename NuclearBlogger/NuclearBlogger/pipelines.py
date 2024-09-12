# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NuclearbloggerPipeline:
    def process_item(self, item, spider):
        # print("title= " + item['title'])
        # print("content= " + item['content'])
        tmp = os.path.curdir + os.path.sep + "result"
        if not os.path.exists(tmp):
            os.makedirs(tmp)
        value = item['title'].replace('/', '、')
        with open(tmp + os.path.sep + value + ".txt", "a+") as f:
            f.write(item['title'])
            f.write("\n\n")
            f.write(item['content'])
            f.close()
        return item
