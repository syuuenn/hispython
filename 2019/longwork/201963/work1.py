# 给定仅有小写字母组成的字符串数组A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
# 例如，如果一个字符在每个字符串中出现
# 3次，但不是4次，则需要在最终答案中包含该字符3次。你可以按任意顺序返回答案。
# 示例
# 1：
# 输入：["bella", "label", "roller"]
# 输出：["e", "l", "l"]
# 示例
# 2：
#
# 输入：["cool", "lock", "cook"]
# 输出：["c", "o"]

# class Solution:
#     def commonChars(self, A):
#         a=set(A[0])
#         s=''
#         for i in a:
#             min=101
#             for j in A:
#                 if j.count(i)<min:
#                     min=j.count(i)
#             s+=i*min
#         print(list(s))
#
# f=Solution()
# f.commonChars(['bella','label','roller'])

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res=[]
        if not A:
            print(res)
        key=set(A[0])
        for k in key:
            minnum=min(a.count(k) for a in A)
            res+=minnum*k
        print(res)

f=Solution()
f.commonChars(['bella','label','roller'])
