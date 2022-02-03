# Time Complexity O(N).
#
# Space Complexity O(1)
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        left, right = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                squ = nums[right]
                right -= 1
            else:
                squ = nums[left]
                left += 1
            res[i] = squ * squ
        return res


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    sol = Solution()
    print(sol.sortedSquares(nums))
