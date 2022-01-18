# Time Complexity O(N)
# Space Complexity O(1)  since we are reusing the input array itself
# as a hash table and the space occupied by the output array doesn't
# count toward the space complexity of the algorithm.
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Iternate over each of the elements in the original array:
        for i in range(len(nums)):
            # Treat the value as the new index
            new_index = abs(nums[i]) - 1
            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative
            # thus indicating that the number nums[i] has
            # appeared or has been visited
            if nums[new_index] > 0:
                nums[new_index] *= -1

        # Response array that would contain the missing numbers
        result = []

        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)

        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(sol.findDisappearedNumbers(nums=nums))
