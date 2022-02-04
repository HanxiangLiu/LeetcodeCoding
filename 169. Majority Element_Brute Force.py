# Time Complexity O(N^2)
# The brute force algorithm contains two nested for loops that each run for n iterations,
# adding up to quadratic time complexity.
#
# Space Complexity O(1)
# The brute force solution does not allocate additional space proportional to
# the input size.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        maj_count = len(nums) // 2
        for n in nums:
            count = sum(1 for elem in nums if elem == n)
            if count > maj_count:
                return n


if __name__ == "__main__":
    nums = [3, 2, 3]
    sol = Solution()
    print(sol.majorityElement(nums))
