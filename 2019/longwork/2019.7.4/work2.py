# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
#
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.


def problem(ls):
    str1 = ''
    count=0
    for i in range(len(ls)):
        str1+=str(ls[i])
        if ls[i]==1:
            count+=1
    str2='1'*count

    for j in range(count):
        if str2 in  str1:
            print(count)
            return
        else:
            count-=1
            str2 = str2[:-1]

problem([1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1])