# 不用循环和条件打印1~1000

# class L(object):
#     def __init__(self,num):
#        self.num = num
#     def __iter__(self):
#         return self
#     def __next__(self):
#         print(self.num)
#
# f = L(5)



# import sys
# sys.setrecursionlimit(1005)
# def printnum(n):
#     print(n)
#     return (n-1000) and printnum(n+1)
#
# printnum(1)


a = [1,2,3]
b=a
a[0]=5
print(b)