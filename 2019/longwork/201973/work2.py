# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# def solutions(num):
#     list1=[]
#     for i in range(num):
#         list1.extend(['(',')'])
#     print(list1)


class Solution:

    def recursive(self, ln, rn, res, prefix):

        if ln == 0 and rn == 1:
            res.append(prefix+')')
            return

        if ln:
            self.recursive(ln-1, rn, res, prefix+'(')

        if prefix[-1] == '(':
            self.recursive(ln, rn-1, res, prefix+')')
        elif rn > ln:
            self.recursive(ln, rn-1, res, prefix+')')

    def generateParenthesis(self, n):

        res = []
        self.recursive(n-1, n, res, '(')
        print(res)

f = Solution().generateParenthesis
f(3)