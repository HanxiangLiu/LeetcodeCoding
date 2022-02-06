# Time Complexity O(N).
# Each number needs to be swapped at most once before it is placed in
# its desired position.
#
# Space Complexity O(1)
# No additional storage is needed (barring the temporary variables
# used for swapping).
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
        return nums[0]


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    sol = Solution()
    print(sol.findDuplicate(nums=nums))
