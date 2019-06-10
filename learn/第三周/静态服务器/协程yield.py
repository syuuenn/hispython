import time
def work1():
    for i in range(5):
        print('work1:',i)
        yield
        time.sleep(0.1)

def work2():
    for i in range(5):
        print('work2:',i)
        yield
        time.sleep(0.1)

# print(work1())
work1=work1()
work2=work2()
for i in range(5):
    next(work1)
    next(work2)



