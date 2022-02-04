# Time Complexity O(N logN)
# Sorting the array costs O(nlgn) time in Python and Java, so
# it dominates the overall runtime.
#
# Space Complexity O(1) or O(N)
# We sorted nums in place here - if that is not allowed, then
# we must spend linear additional space on a copy of nums and
# sort the copy instead.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


if __name__ == "__main__":
    nums = [3, 2, 3]
    sol = Solution()
    print(sol.majorityElement(nums))
