# 反转一个整数，例如123 -->321

def f(num):
    str1=str(num)
    str2=''
    str2=str1[::-1]
    num2=int(str2)
    print(num2)
f(123456)