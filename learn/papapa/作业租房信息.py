#encoding=utf-8
import requests

from bs4 import BeautifulSoup
import csv
url1='https://www.qk365.com/list/'
headers={
    'Referer': 'https://hz.qk365.com/list/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
}

print('***************')
with open('house.csv', 'w', newline='')as f:
    csv_write = csv.writer(f, dialect='excel')
    csv_write.writerow(['户型', '月租', '面积', '朝向', '层数','小区'])

for i in range(1,2):

    print(i)
    url2=url1+'p'+str(i)
    # print(url2)
    r=requests.get(url=url2,headers=headers)
    html_str=r.text
    obj = BeautifulSoup(html_str,'html.parser')
    lists = obj.select('.easyList li a[target="_blank"]')
    # print(lists)
    for j in lists:
        # print(j.attrs['href'])
        try:
            url3=j.attrs['href']
            response = requests.get(url=url3, headers=headers)
            html_str2=response.text
            obj2 = BeautifulSoup(html_str2,'html.parser')
        except:
            break

        ipt_list = []
        list3 = obj2.select('h1[class="houInfoTit"]')

        # print(list3[0].get_text().split(' ')[2])
        try:
            ipt_list.append(list3[0].get_text().split(' ')[2])

            list2 = obj2.select('div[class="survey-left fL"] dd')
        except:
            break

        for x in list2:
            # print(i)
            # print(i.get_text())
            ipt_list.append(x.get_text()[5:])
        # print(ipt_list)
        with open('house.csv', 'a', newline='')as f:
            csv_write = csv.writer(f, dialect='excel')

            csv_write.writerow(ipt_list)