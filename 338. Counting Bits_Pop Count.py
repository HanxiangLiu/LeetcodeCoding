# Time complexity O(N·logN)
#  For each integer x, in the worst case, we need to perform O(logN)
#  operations, since the number of bits in x equals to logx+1 and
#  all the bits can be equal to 1. However, on average, each bit
#  will be set n/2 times, so for each integer x we will perform
#  log(x)/2 operations, therefore, in total, it will cost
#  O(n⋅log(n)/2) operations.
#
# Space complexity O(1)
#  Since the output array does not count towards the space complexity
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = self.pop_count(x)
        return ans

    # same as 191 Number of 1 Bits
    def pop_count(self, x: int) -> int:
        count = 0
        while x != 0:
            x &= x - 1
            # zeroing out the least significant nonzero bit
            count += 1
        return count


if __name__ == "__main__":
    n = 2
    sol = Solution()
    print(sol.countBits(n=n))
