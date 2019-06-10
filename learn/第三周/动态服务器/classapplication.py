import time
import random


def get_time():
    time_data = time.ctime()
    return time_data


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


# 接口

url_list = [('/gettime.exe', get_time), ('/getscore.exe', score)]


# def app(erreron, start_response):
#     request_path = erreron["path"]
#     for path, func in url_list:
#         if request_path == path:
#             start_response('200 ok', [("request_path", request_path)])
#             return func
#
#     else:
#         start_response('404 NOT FOUND', [('server', 'wsgisever')])
#         return '您请求的动态资源不存在'

class App(object):
    def __call__(self,erreron,start_response):
        request_path = erreron["path"]
        for path, func in url_list:
            if request_path == path:
                data = func()
                start_response('200 ok', [("request_path", request_path)])
                return data

        else:
            start_response('404 NOT FOUND', [('server', 'wsgisever')])
            return '您请求的动态资源不存在'
app = App()
