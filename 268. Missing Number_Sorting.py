# Time complexity O(nlgn).
# The only elements of the algorithm that have asymptotically
# non-constant time complexity are the main for loop (which runs
# in O(n) time), and the sort invocation (which runs in O(nlgn) time
# for Python and Java). Therefore, the runtime is dominated by sort,
# and the entire runtime is O(nlgn).
#
# Space complexity O(1) or O(n)
# In the sample code, we sorted nums in place, allowing us to avoid
# allocating additional space. If modifying nums is forbidden, we
# can allocate an O(n) size copy and sort that instead.
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)
        for i, val in enumerate(nums):
            if i != val:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 0, 1]
    print(sol.missingNumber(nums=nums))
