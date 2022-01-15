# time complexity: O(log n). pow method takes log n time.
# space complexity: O(1). Constant space is used

import math


class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        fibn = math.pow((1+math.sqrt(5))/2, n+1) - math.pow((1-sqrt5)/2, n+1)
        return int(fibn/sqrt5)


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(10))
