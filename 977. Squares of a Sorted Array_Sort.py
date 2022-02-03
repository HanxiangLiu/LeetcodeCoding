# Time Complexity O(N logN).
#
# Space Complexity O(N)
# The space complexity of the sorting algorithm depends on
# the implementation of each program language.
# the list.sort() function in Python is implemented with
# the Timsort algorithm whose space complexity is O(N).
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(x*x for x in nums)


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    sol = Solution()
    print(sol.sortedSquares(nums))
