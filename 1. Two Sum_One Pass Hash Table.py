# Time Complexity O(N).
# We traverse the list containing nn elements only once.
# Each lookup in the table costs only O(1) time.
#
# Space Complexity O(N).
# The extra space required depends on the number of items
# stored in the hash table, which stores at most n elements.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))
