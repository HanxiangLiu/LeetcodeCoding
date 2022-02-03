# Time Complexity O(N^2).
# For each element, we try to find its complement by looping
# through the rest of the array which takes O(N) time. Therefore,
# the time complexity is O(N^2)
#
# Space Complexity O(1).
# The space required does not depend on the size of the input
# array, so only constant space is used.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))
