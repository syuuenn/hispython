# 现有不限数量的面额分别为1元，2元， 5元，10元的货币，
# 如果要用这些货币组合成x元，求一共有多少种组合方式？请说出这类问题在算法中被称为什么问题并用代码实现
#w+2y+5z+10r=x
def s(x):
    count=0
    for w in range(x):
        for y in range(x):
            for z in range(x):
                for r in range(x):
                    if w+2*y+5*y+10*r==x:
                        # print(w,y,z,r)
                        count+=1

    print(count)



s(2)