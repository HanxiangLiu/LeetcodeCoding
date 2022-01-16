# Time complexity O(n).
# Although Gauss' formula can be computed in O(1) time,
# summing nums costs us O(n) time, so the algorithm is
# overall linear. Because we have no information about which
# number is missing, an adversary could always design an input
# for which any algorithm that examines fewer than n numbers
# fails. Therefore, this solution is asymptotically optimal.
#
# Space complexity O(1)
# This approach only pushes a few integers around, so it has constant memory usage.
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        exp_sum = len(nums)*(len(nums)+1)//2  # Gauss' Formula
        act_sum = sum(nums)
        return exp_sum - act_sum


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 0, 1]
    print(sol.missingNumber(nums=nums))
