from multiprocessing import Pool
import os
def work(num):
    print(num,'执行',os.getpid())
po=Pool(3)
#print(type(pool))
if __name__ == '__main__':
    for i in range(4):
        po.apply_async(work, (i,))
print('111111111111111111111111111')
po.close()
po.join()
print('222222222222222222222222222')
