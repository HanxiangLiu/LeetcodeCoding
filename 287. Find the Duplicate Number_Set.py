# Time Complexity O(N).
# HashSet insertions and lookups have amortized constant time
# complexities. Hence, this algorithm requires linear time, since it
# consists of a single for loop that iterates over each element,
# looking up the element and inserting it into the set at most once.
#
# Space Complexity O(N)
# We use a set that may need to store at most nn elements, leading to
# a linear space complexity of O(n).
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    sol = Solution()
    print(sol.findDuplicate(nums=nums))
