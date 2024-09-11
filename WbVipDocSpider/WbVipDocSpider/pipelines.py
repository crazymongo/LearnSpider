# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os.path

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WbvipdocspiderPipeline:
    def process_item(self, item, spider):
        # print(item['title'].text)
        tmp = os.path.curdir + os.path.sep + "result"
        if not os.path.exists(tmp):
            os.makedirs(tmp)

        if item['content'] is not None:
            value = item['title'].text.replace('/', '、')
            with open(tmp + os.path.sep + value + ".txt", "a+") as f:
                f.write(item['title'].text)
                f.write("\n\n")
                f.write(item['content'].text)
                f.close()
                with open("complete_set.txt", "a+") as tmp:
                    tmp.write(item['url'])
                    tmp.write("\n")
                    tmp.close()
        else:
            with open("fail_set.txt", "a+") as f:
                f.write(item['url'])
                f.write("\n")
                f.write(item['error_msg'])
                f.write("\n")
                f.write("\n")
                f.close()

        return item

# if __name__ == '__main__':
#     print(os.path.curdir)
