import requests
base_url = 'http://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F&ie=utf-8&pn='
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

for n in range(1,4):
    url = base_url + str((n-1)*50)
    #对应的一级路径的数据
    data = requests.get(url=url,headers=headers)
    #在一级页面匹配图片的地址
    print(data.text)
