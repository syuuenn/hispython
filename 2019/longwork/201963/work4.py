# 一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？
import math
for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if (x**2==i+100)and(y**2==i+268):
        print(i)
