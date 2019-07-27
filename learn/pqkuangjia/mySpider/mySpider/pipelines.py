# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# class MyspiderPipeline(object):
#     def __init__(self):
#         self.file = open('it.csv', 'w', newline='')
#
#     def process_item(self, item, spider):
#         print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
#         l=[]
#         l.append(item)
#         with open('it.csv', 'a', newline='')as f:
#             csv_write = csv.writer(f, dialect='excel')
#             csv_write.writerow(l)
#         return item
import requests
import os
class MyspiderPipeline(object):

    def process_item(self, item, spider):
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

        urls=item['imgurl']
        name=item['xwname']
        print(urls)
        # if not os.path.exists(name):
        #     os.makedirs(name)
        # else:
        #     print('dd')
        # for url in urls:
        #     response=requests.get(url=url)
        #     with open(name+'/'+url[0:]+'.jpg','wb') as f:
        #         f.write((response.content))


        return item