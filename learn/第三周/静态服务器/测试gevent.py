import gevent
from gevent import monkey
import time
monkey.patch_all()


def work1():
    for i in range(5):
        print('work1:',i)
        time.sleep(0.1)

def work2():
    for i in range(5):
        print('work2:',i)
        time.sleep(0.1)


work3=gevent.spawn(work1)
work4=gevent.spawn(work2)
work3.join()
work4.join()

exit()
