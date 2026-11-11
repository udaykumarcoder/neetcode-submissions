class Solution:
    def integerBreak(self, n: int) -> int:
        def dfs(num):
            if num == 1:
                return 1

            if num in dp:
                return dp[num]

            res =  0 if num==n else num

            for i in range(1, num):
                val = dfs(i) * dfs(num-i)
                res = max(res, val)

            dp[num] = res
            return res

        dp = {}
        return dfs(n)