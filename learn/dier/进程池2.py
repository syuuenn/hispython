
from multiprocessing import Manager,Pool
import os
def read(q):
    print('此时readh进程是',os.getpid())
    for i in range(q.qsize()):
        print('此时获取数据',q.get())
def write(q):
    print('此时write进程是',os.getpid())
    for i in range(10):
        q.put(i)
if __name__ == '__main__':
    print(os.cpu_count())
    print("主进程",os.getpid())
    que=Manager().Queue()
    po=Pool()
    po.apply(write,(que,))
    po.apply(read,(que,))
    po.close()
    po.join()
