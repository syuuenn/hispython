import requests
import re
#爬取一级页面，获取到所有的图片地址

url1 ='http://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%B4%E5%83%8F&fr=search'
response = requests.get(url=url1)
html_str = response.text
# print(html_str)
#获取图片地址并保存
exm = '<img src="" attr="79836" data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=6f10d1c6a6d3fd1f365caa38007e0926/12292df5e0fe992551aa2bb83aa85edf8cb171b0.jpg"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=86fb7beb8944ebf86d716437e9c2d52a/b3b7d0a20cf431ad267401d14536acaf2fdd98b0.jpg" '
pat = '<img src="" attr="\d+?" data-original="(http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=.*?.jpg)"  bpic="http://imgsrc.baidu.com/forum/w%3D580%3B/sign=.*?.jpg" '


ret  = re.findall(pattern=pat,string=html_str)
j=0
for i in ret:
    print(i)
#拿出对应的地址，发送请求
    url2 = i
    r=requests.get(url=url2)
    if r.status_code==200:
        jpg_data = r.content
        print(jpg_data)
        with open(str(j)+'.jpg', 'wb+') as f:
            f.write(jpg_data)
            j+=1




#根据拿到的数据