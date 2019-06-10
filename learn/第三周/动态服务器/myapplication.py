import time
import random

# 定义一个存放路径与函数映射的字典
url_func_dict = dict()

#定义装饰器工厂函数
def route(url):
    print(url)
    def warpper(func):
        url_func_dict[url] = func
        print(url_func_dict)
        def inner():
            response_body=func()
            return response_body
        return inner
    return warpper


@route('/login.exe')
def login():
    '''用来处理登录的业务逻辑'''
    print('登录界面')
    return '返回的响应体数据是：登录界面'


@route('/gettime.exe')
def get_time():
    time_data = time.ctime()
    return time_data


@route('/getscore.exe')
def score():
    count = random.randint(30, 100)
    html = '''
       <!DOCTYPE html>
       <html lang="en">
       <head>
           <meta charset="UTF-8">
           <title>Title</title>
       </head>
       <body>
       <h1>your score:%s</h1>

       </body>
       </html>

       ''' % count
    return html


#定义WSGI接口
def app(environ,start_response):

    print('environ:',environ)
    request_path = environ['path']
    print(request_path)

    try:
        start_response('200 ok', [('server', 'wsgisever'), ('name', 'tao'), ('request_path', request_path)])
        reponse_body = url_func_dict[request_path]()
        return reponse_body

    except:#处理找不到路径的情况
        start_response('404 not', [('server', 'wsgisever'), ('name', 'guazi'), ('request_path', request_path)])
        return '找不到页面'






