from multiprocessing import Process
import time
def pri():
    for i in range(1,11):
        print(i)
        print('******************************')
        time.sleep(1)
if __name__ == '__main__':
    pri_proess=Process(target=pri)

    pri_proess.start()
#pri()