# Time complexity O(n).
# Assuming that XOR is a constant-time operation, this
# algorithm does constant work on n iterations, so the runtime is overall linear.
#
# Space complexity O(1)
# This algorithm allocates only constant additional space.
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 0, 1]
    print(sol.missingNumber(nums=nums))
