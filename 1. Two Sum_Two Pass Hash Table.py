# Time Complexity O(N).
# We traverse the list containing N elements exactly twice.
# Since the hash table reduces the lookup time to O(1), the
# overall time complexity si O(N).
#
# Space Complexity O(N).
# The extra space required depends on the number of items
# stored in the hash table, which stores exactly n elements
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))
