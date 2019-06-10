from greenlet import greenlet
def work1():
    for i in range(5):
        print('work1:',i)
        g2.switch()

def work2():
    for i in range(5):
        print('work2:',i)
        g1.switch()
g1=greenlet(work1)
g2=greenlet(work2)
g2.switch()