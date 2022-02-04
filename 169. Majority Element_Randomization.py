# Time Complexity O(inf)
# It is technically possible for this algorithm to run indefinitely
# (if we never manage to randomly select the majority element), so
# the worst possible runtime is unbounded. However, the expected runtime
# is far better - linear, in fact. For ease of analysis, convince yourself
# that because the majority element is guaranteed to occupy more than half
# of the array, the expected number of iterations will be less than it
# would be if the element we sought occupied exactly half of the array.
# Therefore, we can calculate the expected number of iterations for this
# modified version of the problem and assert that our version is easier.
#
# Space Complexity O(1)
# Much like the brute force solution, the randomized approach runs with
# constant additional space.
import random


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        maj_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > maj_count:
                return candidate


if __name__ == "__main__":
    nums = [3, 2, 3]
    sol = Solution()
    print(sol.majorityElement(nums))
