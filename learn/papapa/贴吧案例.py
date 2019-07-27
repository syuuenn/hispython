import requests
url = 'http://imgsrc.baidu.com/forum/w%3D580/sign=c3e5ef1a75899e51788e3a1c72a6d990/793d269759ee3d6da3e4bb2c4d166d224f4ade33.jpg'
response = requests.get(url=url)

print(response)
if response.status_code==200:
    print('编码',response.encoding)
    print('',response.text)
    print(response.content)
    jpg_data = response.content
    with open('a.jpg','wb+') as f:
        f.write(jpg_data)