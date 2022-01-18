# Time complexity O(n^2). We iterate through nums, taking O(n)
# time. We search the whole list to find whether there is duplicate
# number, taking O(n) time. Because search is in the for loop, so we
# have to multiply both time complexities which is O(n^2)
#
# Space complexity O(n). We need a list of size n to contain elements
# in nums.
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 1]
    print(sol.singleNumber(nums))
