# Time Complexity O(N logN)
# Each recursive call to majority_element_rec performs two
# recursive calls on subslices of size 0.5N and two linear
# scans of length N.
#
# Space Complexity O(logN)
# Although the divide & conquer does not explicitly allocate any
# additional memory, it uses a non-constant amount of additional
# memory in stack frames due to recursion. Because the algorithm
# "cuts" the array in half at each level of recursion, it follows
# that there can only be O(lgn) "cuts" before the base case of 1
# is reached. It follows from this fact that the resulting recursion
# tree is balanced, and therefore all paths from the root to a leaf
# are of length O(lgn). Because the recursion tree is traversed in
# a depth-first manner, the space complexity is therefore equivalent
# to the length of the longest path, which is, of course, O(lgn).
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of
            # size 1 is the majority element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two valves agree on the majority element, return it.
            if left == right:
                return left

            # Otherwise, count each element and return the winner
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)


if __name__ == "__main__":
    nums = [3, 2, 3]
    sol = Solution()
    print(sol.majorityElement(nums))
