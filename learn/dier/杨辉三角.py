def yanghui(t):
    print ([1])
    line = [1,1]
    print(line)
    for i in range(2,t):
        r = []
        for i in range(0,len(line)-1):
         r.append(line[i]+line[i+1])
         line = [1]+r+[1]
        print(line)



yanghui(10)
#修改


