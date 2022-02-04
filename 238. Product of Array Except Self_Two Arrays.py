# Time complexity O(N), where N represents the number of elements in the
# input array. We use one iteration to construct the array Left, one to
# construct the array Right and one last to construct the answer array
# using Left and Right.
#
# Space Complexity O(N). used up by the two intermediate arrays that we
# constructed to keep track of product of elements to the left and right
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # The length of the input array
        length = len(nums)

        # The left and right arrays as described in the algorithm
        left, right, answer = [0]*length, [0]*length, [0]*length

        # left[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to
        # the left, so the left[0] would be 1
        left[0] = 1
        for i in range(1, length):
            # left[i-1] already contains the product of elements to the
            # left of 'i-1'. Simply multiplying it with nums[i-1] would
            # give the product of all elements to the left of index 'i'
            left[i] = nums[i-1] * left[i-1]

        # Right[i] contains the product of all the elements to the right
        # Note: for the element at index 'length-1', there are no elements
        # to the right, so the right[length-1] would be 1
        right[length-1] = 1
        for i in reversed(range(length - 1)):
            # right[i+1] already contains the product of elements to the
            # right of 'i+1'. Simply multiplying it with nums[i+1] would
            # give the product of all elements to the right of index 'i'
            right[i] = nums[i + 1] * right[i + 1]

        # Constructing the answer array
        for i in range(length):
            # For the first element, right[i] would be product except self
            # For the last element, product except self would be left[i]
            # Else, multiple product of all elements to left and to the right
            answer[i] = left[i] * right[i]

        return answer


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    sol = Solution()
    print(sol.productExceptSelf(nums))
