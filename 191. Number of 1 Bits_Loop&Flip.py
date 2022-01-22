# Time complexity O(1).
# The rum time depends on the number of bits in n, and n is a
# 32-bit integer.
# Space complexity O(1).
# no additional space is allocated.
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        # 注意这里的=号
        while mask <= n:
            if (n & mask) != 0:
                bits += 1
            mask <<= 1
        return bits


if __name__ == "__main__":
    n = 11
    sol = Solution()
    print(sol.hammingWeight(n))

