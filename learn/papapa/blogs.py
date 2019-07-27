import requests

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
for i in range(0,240):
    url='https://blog.csdn.net/syuuenn/article/details/95353046'
    r = requests.get(url=url,headers=headers)
    print(i)