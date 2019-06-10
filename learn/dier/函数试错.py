def countsum(a,b):
    sum=a+b
    return sum


try:
    c=countsum(2,2)
    print(c)
except Exception as e:
    print('false')
else:
    print('no false')
finally:
    print('最后')