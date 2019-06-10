'''应用程序框架'''
#WSGI接口
def app(environ,start_response):
    '''
    :param environ:和HTTP请求相关数据（请求路径和用户请求头），字典
    :param start_response:函数引用（由服务器提供，作用：设置状态和响应头）
    start_response这个方法：函数有两个参数，第一表示状态，第二表示响应头（类型：列表），写在服务器上，但是程序框架可以调用
    :return:
    '''
    start_response()
    return 'hello world from WSGI'