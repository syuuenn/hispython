import threading
def working():
    for i in range(5):
        print('工作')

def playing():
    for i in range(5):
        print('玩乐')
working_thread = threading.Thread(target=working)
playing_thread = threading.Thread(target=playing)

if __name__ == '__main__':
    working_thread.setDaemon(True)
    working_thread.start()
    playing_thread.start()




