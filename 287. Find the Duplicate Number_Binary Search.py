# Time Complexity O(NlogN).
# The outer loop uses binary search to identify a candidate - this
# runs in O(logn) time. For each candidate, we iterate over the entire
# array which takes O(n) time, resulting in a total of O(nlogn) time.
#
# Space Complexity O(1)
# No additional storage is needed (barring a few variables), resulting
# in a constant O(1) space complexity.
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # 'low' and 'high' represent the range of values of the target.
        low, high = 1, len(nums) - 1
        duplicate = -1
        while low <= high:
            count, cur= 0, (low + high) // 2
            # count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
        return duplicate


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    sol = Solution()
    print(sol.findDuplicate(nums=nums))
