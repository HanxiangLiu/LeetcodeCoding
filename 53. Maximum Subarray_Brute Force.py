# Time Complexity: O(n^2), where n is the length of nums.
# We use 2 nested for loops, with each loop iterating
# through nums.
#
# Space complexity: O(1). No matter how big the input is,
# we are only ever using 2 variables.
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_num = nums[0]
        # max_num = -math.inf
        for i in range(len(nums)):
            sum_i = nums[i]
            max_num = max(max_num, sum_i)
            for j in range(i+1, len(nums)):
                sum_i += nums[j]
                max_num = max(max_num, sum_i)
        return max_num


if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(nums=nums))
