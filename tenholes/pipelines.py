# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os


class TenholesPipeline:
    def __init__(self):
        filedir = './data/'
        filename = 'article3.txt'
        if not os.path.exists(filedir):
            os.mkdir(filedir)
        filepath = filedir + filename
        self.fp = open(filepath,'a+',encoding='utf-8')

    def process_item(self, item, spider):
        try:
            id = '编号：'+item['id']+'\t'
            title = '标题：'+item['title']+'\t'
            time = '日期：'+item['time']+'\t'
            content = '内容：'+item['content'] + '\n'
            line = [id,time,title,content]

            self.fp.writelines(line)
            print('编号{}文章爬取成功！'.format(id))
        except:
            print('编号{}文章不存在！'.format(id))
        return item
