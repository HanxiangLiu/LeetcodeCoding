# Time complexity O(nlogn).Sorting is O(nlogn) and the sweeping is O(n). The entire algorithm
# is dominated by the sorting step, which is O(nlogn).
# Space complexity O(1). Space depends on the sorting implementation which, usually,
# O(1) auxiliary space if heapsort is used.
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.containsDuplicate(nums=nums))

# The implementation here modifies the original array by sorting it.
# In general, it is not a good practice to modify the input unless
# it is clear to the caller that the input will be modified.
# One may make a copy of nums and operate on the copy instead.
