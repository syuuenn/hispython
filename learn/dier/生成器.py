def F(num):
    a=0
    b=1
    current_index=0
    while current_index<num:
        result = a
        a,b=b,a+b
        current_index +=1
        paroms = yield result
        print('参数',paroms)


if __name__ == '__main__':
    ret= F(5)
    print(ret.send(None))
    # print(next(ret))
    # print(next(ret))
    # print(next(ret))
    for num in ret:
        print(num)

    print("*************************************")
    print(ret.send('dgf'))

