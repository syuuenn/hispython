# 判断101-200之间有多少个素数，并输出所有素数
count = 0
for i in range(101,201):
    a = 0
    for j in range(2,i):
        if(i%j==0):
            a+=1
    if(a==0):
        count+=1
        print(i)
print(count)
