# time complexity: O(n). Size of recursion tree can go upto n.
# Space complexity: O(n). The depth of recursion tree can go upto n.

# BV1AB4y1w7eT
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        return self.climbstairs(i=0, n=n, memo=memo)

    def climbstairs(self, i: int, n: int, memo: list[int]) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climbstairs(i=i + 1, n=n, memo=memo) + \
                  self.climbstairs(i=i + 2, n=n, memo=memo)
        return memo[i]


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(10))
