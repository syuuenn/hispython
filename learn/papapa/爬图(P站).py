import requests
import re

#爬取一级页面，获取到所有的图片地址
base_url='http://acg17.com/tag/pixiv'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
j=1
for i in range(1,15):

    url1 =base_url+'/page/'+str(i)+'/'

    response = requests.get(url=url1,headers=headers)
    html_str = response.text
    # print(html_str)
#获取图片地址并保存
# exm = '<img width="310" height="165" style="background:url(https://ae01.alicdn.com/kf/HTB1rkGgabr1gK0jSZR0q6zP8XXa1.jpg) no-repeat center center" '

    pat = '<img width="310" height="165" style="background:url\((.*?)\)'



    ret  = re.findall(pattern=pat,string=html_str)

    for i in ret:
        print(i)
    #拿出对应的地址，发送请求
        url2 = i
        r=requests.get(url=url2)
        if r.status_code==200:
            jpg_data = r.content
            print(jpg_data)
            with open('pic/'+str(j)+'.jpg', 'wb+') as f:
                f.write(jpg_data)
                j+=1