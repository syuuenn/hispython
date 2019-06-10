class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        for i in range(1, n+1):
            dp.append(min(dp[-j**2] for j in range(1, 1 + int(i**0.5))) + 1)
        return dp[-1]
f=Solution()
print(f.numSquares(12))