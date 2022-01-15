# Time complexity O(n). We do search() and insert() for n times
# and each operation takes constant time.
# Space complexity O(n). The space used by a hash table is linear
# with the number of elements in it.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        mapNums = dict()
        for i in nums:
            if i in mapNums:
                return True
            mapNums[i] = 1
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 1]
    print(sol.containsDuplicate(nums=nums))


# For certain test cases with not very large nn, the runtime of this
# method can be slower than Sorting Approach. The reason is hash table
# has some overhead in maintaining its property. One should keep in
# mind that real world performance can be different from what the Big-O
# notation says. The Big-O notation only tells us that for sufficiently
# large input, one will be faster than the other. Therefore, when n is not
# sufficiently large, an O(n) algorithm can be slower than an
# O(nlogn) algorithm.
