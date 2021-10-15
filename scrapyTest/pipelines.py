# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class ScrapytestPipeline:
    def process_item(self, item, spider):
        return item
class FianacespiderPipeline:
    def process_item(self, item, spider):
        with open("result.csv","a+",encoding="utf-8") as f:
            w = csv.writer(f)
            row = item['游戏地址'],item['游戏图片'],item['游戏名字'],item['游戏类型']
            w.writerow(row)
            print("已保存")
        return item

class savefileTongscrapyPipeline(object):
    def __init__(self):
        self.file = open('py51jobsinfo.csv', 'w', newline='')
        self.csvwriter = csv.writer(self.file)
        self.csvwriter.writerow(['游戏名字', '游戏类型', '游戏图片', '游戏地址'])
    def process_item(self, item, spider):
        self.csvwriter.writerow([item["游戏名字"], item["游戏类型"], item["游戏图片"], item["游戏地址"]])
        print(';;;;;;;;;;;;;;;;;;')
        return item
    def close_spider(self, spider):
        self.file.close()