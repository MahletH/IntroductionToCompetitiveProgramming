class Solution:        
    def integerBreak(self, n: int) -> int:
        dp = [1,1]
        for i in range(2,n+1):
            max_ = 0
            for j in range(1,i//2+1):
                res = max(dp[j],j) * max(dp[i -j],i - j)
                max_ = max(max_, res)
            dp.append(max_)        
        return dp[n]
