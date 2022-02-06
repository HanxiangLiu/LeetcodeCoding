# Time Complexity O(N).
# Each element is visited at most twice (once in the first loop to find
# the duplicate and once in the second loop to restore the numbers).
#
# Space Complexity O(1)
# All manipulation is done in place, so no additional storage (barring
# one variable) is needed.
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        duplicate = -1
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -nums[cur]

        # Restore numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    sol = Solution()
    print(sol.findDuplicate(nums=nums))
