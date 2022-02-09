# Time Complexity O(NlogN)
# A performant comparison-based sorting algorithm will run in O(nlogn) time.
# Note that this can be reduced to O(n) using a special sorting algorithm
# like Radix Sort.
# Traversing the array after sorting takes linear time i.e. O(n).
#
# Space Complexity O(1).
# No extra space required, other than the space for the output list.
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        try:
            nums[1]
        except IndexError:
            return []
        else:
            ans = []
            nums.sort()
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1]:
                    ans.append(nums[i])
            return ans


if __name__ == "__main__":
    # nums = [4, 3, 2, 7, 8, 2, 3, 1]
    nums = [1]
    sol = Solution()
    print(sol.findDuplicates(nums))
