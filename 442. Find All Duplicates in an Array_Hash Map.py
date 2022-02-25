# Time Complexity O(N) average case. O(n^2) worst case.
# It takes a linear amount of time to iterate through the array.
# Lookups in a hashset are constant time on average, however those can degrade
# to linear time in the worst case. Note that an alternative is to use
# tree-based sets, which give logarithmic time lookups always.
#
# Space Complexity Upto O(n) extra space required for the set.
# If you are tight on space, you can significantly reduce your physical space
# requirements by using bitsets [1] instead of sets. This data-structure
# requires just one bit per element, so you can be done in just nn bits of data
# for elements that go up-to n. Of course, this doesn't reduce your space
# complexity: bitsets still grow linearly with the range of values that the
# elements can take.
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans = []
        seen = {}

        for num in nums:
            if num in seen:
                ans.append(num)
            seen[num] = 1

        return ans


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    # nums = [1]
    sol = Solution()
    print(sol.findDuplicates(nums))
