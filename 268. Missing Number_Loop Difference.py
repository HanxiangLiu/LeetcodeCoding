# Time complexity O(n).
#
# Space complexity O(1)
# it has constant memory usage.
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = 0 + len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 0, 1]
    print(sol.missingNumber(nums=nums))
