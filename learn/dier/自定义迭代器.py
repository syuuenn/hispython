class MyIterater:
    def _init_(self,items):
        self.items=items
        self.current_index=0

    def _iter_(selfself):
       pass

    class MyList:
        def __init__(self):
            self.items = list()

        # 增加元素的功能
        def append_item(self, obj):
            self.items.append(obj)

        # 添加__iter__这个魔法方法，表示对象那个可以迭代

        def __iter__(self):
            '''需要返回的是一个迭代器'''
            myiterator = MyIterater(self.items)
            return myiterator
            pass
    def _next_(self):
        if self.current_index<len(self.items):
            value=self.items[self.current_index]
            self.current_index+=1
            return value
        else:
            raise StopIteration
        mylist = MyList()
        mylist.append_item('java')
        mylist.append_item('python')
        print(mylist)
        ret = isinstance(mylist, Iterable)
        print('判断mylist是否可以被迭代', ret)
        for i in mylist:
            print(i)