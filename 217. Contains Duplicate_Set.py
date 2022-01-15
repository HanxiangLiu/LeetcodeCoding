# Time complexity O(n)
# Space complexity O(n). For using set.
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.containsDuplicate(nums=nums))
