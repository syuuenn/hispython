url_func_dict = {}
def route(url):
    def warpper(func):
        url_func_dict[url] = func
        def inner():
            response_body = func()
            return response_body
        return inner
    return warpper

@route('/login.exe')
def login():
    print("登陆页面")
    return "登陆页面"

class App(object):
    def __call__(self,environ,start_response):
        request_path = environ['path']

        try:
            start_response('200 ok',[('path',request_path)])
            response_body = url_func_dict[request_path]()
            return response_body
        except:
            start_response('404 not found',[('path',request_path)])
            return '页面找不到'
app = App()