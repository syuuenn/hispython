
# 采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
# 加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三 位交换。
def f(num):
    s1=str(num)
    list1=[]
    for i in range(4):
        new_num=(int(s1[i])+5)%10
        list1.append(str(new_num))
    list1.reverse()
    str1=''.join(list1)
    print(int(str1))
f(1234)


