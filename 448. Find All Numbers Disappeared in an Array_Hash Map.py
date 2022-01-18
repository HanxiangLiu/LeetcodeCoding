# Time Complexity O(N)
# Space Complexity O(N)
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Hash table for keeping track of the numbers in the array
        # Note that we can also use a set here since we are not
        # really concerned with the frequency of numbers.
        hash_table = {}

        # Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1

        # Response array that would contain the missing numbers
        result = []

        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table.
        for num in range(1, len(nums)+1):
            if num not in hash_table:
                result.append(num)

        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(sol.findDisappearedNumbers(nums=nums))
