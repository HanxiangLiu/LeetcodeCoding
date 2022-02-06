# Time Complexity O(N).
# The function (store) makes a single recursive call at every
# instance. Each index is visited at most once, resulting in O(n)
# time complexity.
#
# Space Complexity O(N)
# Since this is a recursive function with up to n self-invocations
# (i.e. depth of the recursive function = n), the space complexity is
# O(n) as there can be up to n function calls in memory at some point.
# Note that due to the recursive nature of the solution, there is some
# additional overhead on each invocation (such as the function variables
# and a return function pointer that are stored on the system executable
# stack).
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        def store(nums: list[int], cur:int) -> int:
            if cur == nums[cur]:
                return cur
            nxt, nums[cur] = nums[cur], cur
            return store(nums, nxt)

        return store(nums, 0)


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    sol = Solution()
    print(sol.findDuplicate(nums=nums))
