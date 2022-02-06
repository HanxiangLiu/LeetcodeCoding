# Time Complexity O(NlogN).
# Sorting takes O(NlogN) time. This is followed by a linear scan, resulting
# in a total of O(NlogN) + O(N) = O(NlogN) time.
#
# Space Complexity O(logN) or O(N)
# The space complexity of the sorting algorithm depends on the implementation
# of each programming language:
# 1. In Java, Arrays.sort() for primitives is implemented using a variant
# of the Quick Sort algorithm, which has a space complexity of O(logn)
# 2. In C++, the sort() function provided by STL uses a hybrid of Quick
# Sort, Heap Sort and Insertion Sort, with a worst case space complexity
# of O(logn)
# 3. In Python, the sort() function is implemented using the Timsort
# algorithm, which has a worst-case space complexity of O(n)
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    sol = Solution()
    print(sol.findDuplicate(nums=nums))
