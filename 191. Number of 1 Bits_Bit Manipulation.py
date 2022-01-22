# Time complexity O(1).
# The rum time depends on the number of bits in n, and n is a
# 32-bit integer.
# Space complexity O(1).
# no additional space is allocated.
class Solution:
    def hammingWeight(self, n: int) -> int:
        times = 0
        while n != 0:
            times += 1
            n &= (n - 1)
        return times


if __name__ == "__main__":
    n = 11
    sol = Solution()
    print(sol.hammingWeight(n))
