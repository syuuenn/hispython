# 给定一个矩阵A， 返回A的转置矩阵。
# 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
#
#
#
# 示例1：
# 输入：[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出：[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#
# 示例2：
# 输入：[[1, 2, 3], [4, 5, 6]]
# 输出：[[1, 4], [2, 5], [3, 6]]

# import numpy
# a=numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a.T)



# def f(param):
#     list1=[]
#     list2=[]
#     for i in range(len(param)):
#         list2.append(0)
#     for j in range(len(param)):
#         list1.append(list2)
#     list3=str(list1)
#     list4=[]
#     print(list3)
#     # for i in range(len(list3)):
#     #     if list3[i]!='[' or list3[i]!=']':
#     #         list4.append(int(list3[i]))
#     #
#     # for m in range(len(param)):
#     #     for n in range(len(param)):
#     #        list4[n][m]=param[m][n]
#     #         # print(param[m][n])
#     # print(list4)
#     # print(list2)
#
#
# f([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


class Solution:
    def transpose(self, A):
        result = []
        for i in range(len(A[0])):
            result.append([])
            for j in range(len(A)):
                result[i].append(A[j][i])
        return result

f=Solution()
print(f.transpose([[1, 2, 3], [4, 5, 6]]))