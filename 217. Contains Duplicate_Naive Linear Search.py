# Time complexity O(n^2).  In the worst case, there are (n(n-1))/2 pairs of integers to check.
# Therefore, the time complexity is O(n^2).
# Space complexity O(1). We only used constant extra space.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] == nums[i]:
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.containsDuplicate(nums=nums))
