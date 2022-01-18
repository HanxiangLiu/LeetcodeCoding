# Time Complexity: O(n), where n is the length of nums.
# We iterate through every element of nums exactly once.
#
# Space complexity: O(1). No matter how big the input is,
# we are only ever using 2 variables.
#
# Whenever you see a question that asks for the maximum
# or minimum of something, consider Dynamic Programming
# as a possibility.
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]
        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # if current_subarray is negative, throw it away.
            # Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray


if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(nums=nums))
