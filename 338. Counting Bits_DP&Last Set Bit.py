# Time complexity O(N)
# For each integer x, in the range 1 to n, we need to perform a
# constant number of operations which does not depend on the
# number of bits in x.
#
# Space complexity O(1)
# Since the output array does not count towards the space complexity
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans


if __name__ == "__main__":
    n = 2
    sol = Solution()
    print(sol.countBits(n=n))
