# Time Complexity O(N)
# Space Complexity O(N)
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set(range(1, len(nums)+1)).difference(set(nums)))


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(sol.findDisappearedNumbers(nums=nums))
