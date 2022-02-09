# Time Complexity O(N^2)
# For each element in the array, we search for another occurrence in the rest
# of the array. Hence, for the ith element in the array, we might end up looking
# through all n - i remaining elements in the worst case. So, we can end up
# going through about n^2 elements in the worst case.
#
# Space Complexity O(1).
# No extra space required, other than the space for the output list.
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i]:
                    ans.append(nums[i])
                    break
        return ans


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    sol = Solution()
    print(sol.findDuplicates(nums))
