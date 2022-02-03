# Time Complexity O(N*logN).
#
# Space Complexity O(N).
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr = []
        for i, x in enumerate(nums):
            arr.append([x, i])
        arr.sort()  # Sort arr in increasing order by their values.

        left, right = 0, len(arr) - 1
        while left < right:
            twosum = arr[left][0] + arr[right][0]
            if twosum == target:
                return [arr[left][1], arr[right][1]]
            elif twosum > target:
                right -= 1
            else:
                left += 1


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))
