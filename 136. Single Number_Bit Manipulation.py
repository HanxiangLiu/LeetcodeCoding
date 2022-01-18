# Time complexity O(n). We only iterate through nums,
# so the time complexity is the number of elements in nums.
#
# Space complexity O(1).
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 1]
    print(sol.singleNumber(nums))
