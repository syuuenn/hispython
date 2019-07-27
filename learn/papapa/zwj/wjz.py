# coding=utf-8
import requests
from bs4 import BeautifulSoup
import csv

url_first = 'http://hz.ganji.com/chuzu/'
url_list = 'pn'

headers ={ "Proxy-Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
with open('杭州.csv', 'w', newline='')as f:
    csv_write = csv.writer(f, dialect='excel')
    csv_write.writerow(['城市', '区域', '小区名称', '户型分类','户型类型', '面积','装修类型','价格','付款方式','更新时间'])
    a = 1
for n in range(1,71):
    try:
        url = url_first+url_list+str(n)+'/'
        data_obj = requests.get(url=url,headers=headers)
        data_text = data_obj.text
        # print(data_text)
        data_doc = BeautifulSoup(data_text)
        href_first_1 = data_doc.select('dl[class="f-list-item-wrap min-line-height f-clear"] dd[class="dd-item title"] a')
        # print(href_first_1)
        # print(a)
        a+=1
        for i in range(len(href_first_1)):
            try:
                href_first = href_first_1[i].attrs['href']
                # print(href_first)
                requests_info = requests.get(url=href_first, headers=headers)
                data_text_info = requests_info.text
                data_doc_info = BeautifulSoup(data_text_info)
                # 城市
                city = data_doc_info.select('div[class="city"] a')[0].get_text()
                # 区域
                area = data_doc_info.select('div[class="district"] ul[class="info f-clear"] li')[1].get_text().split()[-3]
                # 小区名称
                village = data_doc_info.select('div[class="district"] p[class="title"] a span')[0].get_text()
                # 户型分类
                type = data_doc_info.select('ul[class="er-list f-clear"] li[class="item f-fl"] span[class="content"]')[0].get_text()
                # 户型类型
                apartment = '1.标准平面'
                # 面积
                measure = data_doc_info.select('ul[class="er-list f-clear"] li[class="item f-fl"] span[class="content"]')[1].get_text().split()[-1]
                # 装修类型
                renovation = data_doc_info.select('ul[class="er-list f-clear"] li[class="item f-fl"] span[class="content"]')[4].get_text()
                # 价格
                price = data_doc_info.select('div[class="card-top"] div[class="er-card-pay"] div[class="price-wrap"] span')[0].get_text() + '元/月'
                # 付款方式
                payment = data_doc_info.select('div[class="card-top"] div[class="er-card-pay"] div[class="price-wrap"] span')[1].get_text()
                # 更新时间
                time = data_doc_info.select('div[class="card-status f-clear"] ul[class="card-status-left f-fl"] li[class="date"]')[0].get_text()
                ipt_list = [city,area,village,type,apartment,measure,renovation,price,payment,time]
                print('我进去了')
                try:
                    with open('杭州.csv', 'a', newline='')as f:
                        csv_write = csv.writer(f, dialect='excel')

                        csv_write.writerow(ipt_list)
                except:
                    print('保存未成功')

            except:
                print('#################网址进不去####################')
                # print(href_first_1)
                print('网址进不去')
                break
    except:
        print('主页进不去')
        break