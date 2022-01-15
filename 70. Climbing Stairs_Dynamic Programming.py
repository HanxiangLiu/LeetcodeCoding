# Time complexity: O(n). Single loop upto nn.
# Space complexity: O(n). dp array of size n is used.
# BV1AB4y1w7eT
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(10))
