# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


# def combinationSum(candidates, target):
#     candidates.sort()
#     n = len(candidates)
#     res = []
#     def helper(i, tmp_sum, tmp):
#         if tmp_sum > target or i == n:
#             return
#         if tmp_sum == target:
#             res.append(tmp)
#             return
#         helper(i,  tmp_sum + candidates[i],tmp + [candidates[i]])
#         helper(i+1, tmp_sum ,tmp)
#     helper(0, 0, [])
#     print(res)
#
#
# combinationSum([2,3,5],8)

class Solution:
    def combinationSum(self, nums, target):
        nums.sort()
        res=list()
        st=list()
        n=len(nums)
        i=0
        while True:
            if target==0:
                res.append([nums[i] for i in st])
                i=st.pop()
                target+=nums[i]
                i+=1
            elif i==n or nums[i]>target:
                if len(st)==0:
                    return res
                i=st.pop()
                target+=nums[i]
                i+=1
            elif nums[i]<=target:
                st.append(i)
                target-=nums[i]



f = Solution()
f.combinationSum([2,3,5],8)



