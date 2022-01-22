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
        x = 0
        b = 1

        # [0, b) is calculated
        while b <= n:
            # generate [b, 2b) or [b, n) from [0, b)
            while x < b and x + b <= n:
                ans[x + b] = ans[x] +1
                x += 1
            x = 0  # reset x
            b <<= 1  # b = 2b

        return ans


if __name__ == "__main__":
    n = 2
    sol = Solution()
    print(sol.countBits(n=n))
