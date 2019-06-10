import threading
lock=threading.Lock()
lock.acquire()
lock.release()
num=0
def f1():
    x=0
    global num
    while x<=1000000:
        r=lock.acquire()
        if r:
         num+=1
         x+=1
        lock.release()
    print(num)

def f2():
    y=0
    global num
    while y<=1000000:
        r = lock.acquire()
        if r:
            num += 1
            y++1
        lock.release()
    print(num)
if __name__ == '__main__':
    f1_thread=threading.Thread(target=f1)
    f2_thread=threading.Thread(target=f2)

    f1_thread.start()
    f2_thread.start()

