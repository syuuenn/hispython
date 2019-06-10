import threading
g_num=0
lock=threading.Lock()
lock.acquire()
lock.release()

def f1(num):
    global g_num
    for i in range(num):
        ret=lock.acquire()
        if ret:
            g_num+=i
            lock.release()
    print('f1等于:',g_num)

def f2(num):
    global g_num
    for i in range(num):
        ret = lock.acquire()
        if ret:
            g_num += i
            lock.release()
    print('f2等于:',g_num)

if __name__ == '__main__':
    f1_thread=threading.Thread(target=f1,args=(1000,))
    f2_thread=threading.Thread(target=f2,args=(1000,))

    f1_thread.start()
    # f1_thread.join()
    f2_thread.start()