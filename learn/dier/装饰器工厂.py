# 根据参数不同，生产不同的装饰器
def factory(arg=None):    #工厂函数
    def timefun(func):   #装饰器
        def inner():
            if arg:
                print('有')
            else:
                print('没')
            return func()
        return inner
    return timefun

@factory(1)     #这里的（）一定要有
def f():
    print('f')

f()
