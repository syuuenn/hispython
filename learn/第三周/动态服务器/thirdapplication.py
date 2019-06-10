url_func_dict = dict()
def route(url):
    def warpper(func):
        url_func_dict[url] = func
        def inner():
            respond_body = func()
            return respond_body
        return inner()
    return warpper

@route('/login.exe')
def login():
    return '登陆页面'

class App(object):
    def __call__(self,environ,start_respond):
        request_path = environ["path"]
        try:
            start_respond('200 ok',[('path',request_path)])
            respond_body = url_func_dict[request_path]()
            return respond_body
        except:
            start_respond('404 not',[('path',request_path)])
            return '找不到'
app = App()