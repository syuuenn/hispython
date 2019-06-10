import threading
lock=threading.Lock()
lock.acquire()
lock.release()
a,b,c,d,e=0,0,0,0,0
def eating(name):
    print( name+"吃饭")
def noeating():
    print('不吃饭')

def f1():
    global a
    ret=lock.acquire()
    if ret:
        global b
        ret=lock.acquire( )
        if ret:
            eating(1)
            lock.release()
            lock.release()
    else:
        noeating(1)
def f2():
    global b
    ret = lock.acquire()
    if ret:
        global c
        ret = lock.acquire()
        if ret:
            eating(2)
            lock.release()
            lock.release()
    else:
        noeating(2)
def f3():
    global c
    ret = lock.acquire()
    if ret:
        global d
        ret = lock.acquire()
        if ret:
            eating(3)
            lock.release()
            lock.release()
    else:
        noeating(3)
def f4():
    global d
    ret = lock.acquire()
    if ret:
        global e
        ret = lock.acquire()
        if ret:
            eating(4)
            lock.release()
            lock.release()
    else:
        noeating(4)
def f5():
    global e
    ret = lock.acquire()
    if ret:
        global a
        ret = lock.acquire()
        if ret:
            eating(5)
            lock.release()
            lock.release()
    else:
        noeating(5)

if __name__ == '__main__':
    f1_thread = threading.Thread(target=f1)
    f2_thread = threading.Thread(target=f2)
    f3_thread = threading.Thread(target=f3)
    f4_thread = threading.Thread(target=f4)
    f5_thread = threading.Thread(target=f5)

    f1_thread.start()
    f2_thread.start()
    f3_thread.start()
    f4_thread.start()
    f5_thread.start()






