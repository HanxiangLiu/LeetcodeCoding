# time complexity: O(n). Single loop upto n is required to calculate nth fibonacci number.
# space complexity: O(1). Constant space is used
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            first, second = second, first + second
        return second


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(10))
