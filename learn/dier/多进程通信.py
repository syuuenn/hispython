from multiprocessing import Process, Queue, Lock

L = [1, 2, 3]


def add(q, lock, a, b):
    lock.acquire()  # 加锁避免写入时出现不可预知的错误
    L1 =list(range(a, b))
    lock.release()
    q.put(L1)
    print (L1)

if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    p1 = Process(target=add, args=(q, lock, 20, 30))
    p2 = Process(target=add, args=(q, lock, 30, 40))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    L +=q.get() + q.get()
    print (L)
