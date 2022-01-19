# Time Complexity: O(N·logN), where N is the length of nums.
#
# Space complexity: O(logN), where N is the length of nums.
import math


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return self.findBestSubarray(nums, 0, len(nums)-1)

    def findBestSubarray(self, nums: list[int], left: int, right: int) -> int:
        # Base case - empty array
        if left > right:
            return -math.inf

        mid = (left + right) // 2
        curr = best_left_sum = best_right_sum = 0

        # Iterate from the middle to the beginning.
        for i in range(mid-1, left-1, -1):
            curr += nums[i]
            best_left_sum = max(best_left_sum, curr)

        # Reset curr and iterate from the middle to the end
        curr = 0
        for i in range(mid+1, right+1):
            curr += nums[i]
            best_right_sum = max(best_right_sum, curr)

        # The best_combined_sum uses the middle element and
        # the best possible sum from each half
        best_combined_sum = nums[mid] + best_left_sum + best_right_sum

        # Find the best subarray possible from both halves
        left_half = self.findBestSubarray(nums, left, mid-1)
        right_half = self.findBestSubarray(nums, mid+1, right)

        # The largest of the 3 is the answer for any given input array
        return max(best_combined_sum, left_half, right_half)


if __name__ == "__main__":
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(nums=nums))

# On our first call to findBestSubarray, we use for loops to visit
# every element of nums. Then, we split the array in half and call
# findBestSubarray with each half. Both those calls will then iterate
# through every element in that half, which combined is every element
# of nums again. Then, both those halves will be split in half, and 4
# more calls to findBestSubarray will happen, each with a quarter of
# nums. As you can see, every time the array is split, we still need
# to handle every element of the original input nums. We have to do
# this logN times since that's how many times an array can be split
# in half.
#
# The extra space we use relative to input size is solely occupied by
# the recursion stack. Each time the array gets split in half, another
# call of findBestSubarray will be added to the recursion stack, until
# calls start to get resolved by the base case - remember, the base
# case happens at an empty array, which occurs after logN calls.
