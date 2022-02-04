# Time complexity O(N), where N represents the number of elements in the
# input array. We use one iteration to construct the array Left, one to
# construct the array Right and one last to construct the answer array
# using Left and Right.
#
# Space complexity : O(1) since don't use any additional array for
# our computations. The problem statement mentions that using the
# answer array doesn't add to the space complexity.
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0] * length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):
            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    sol = Solution()
    print(sol.productExceptSelf(nums))
