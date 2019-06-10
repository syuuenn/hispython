import threading
it=[]
def it_write():
    for x in range(5):
        it.append(x)

def it_read():
        print(it)

if __name__ == '__main__':
    it_write_thread=threading.Thread(target=it_write)
    it_read_thread=threading.Thread(target=it_read)

    it_write_thread.start()
    it_write_thread.join()
    it_read_thread.start()