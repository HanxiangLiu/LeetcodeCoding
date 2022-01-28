# Time Complexity O(logN).
# Space Complexity O(1) since it's a constant space solution.
import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return bisect.bisect(nums, target)


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    sol = Solution()
    print(sol.search(nums=nums, target=target))
