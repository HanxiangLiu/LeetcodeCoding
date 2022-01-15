# time complexity: O(2^n). Size of recursion tree will be 2^n
# Space complexity: O(n). The depth of the recursion tree can go upto n.

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbstairs(i=0, num=n)

    def climbstairs(self, i: int, num: int) -> int:
        if i > num:
            return 0
        if i == num:
            return 1
        back = self.climbstairs(i=i + 1, num=num) + self.climbstairs(i=i + 2, num=num)
        return back


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(10))
