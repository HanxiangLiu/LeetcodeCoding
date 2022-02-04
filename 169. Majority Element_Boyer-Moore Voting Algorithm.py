# Time Complexity O(N)
# Boyer-Moore performs constant work exactly nn times,
# so the algorithm runs in linear time.
#
# Space Complexity O(1)
# Boyer-Moore allocates only constant additional memory.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count, candidate = 0, None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


if __name__ == "__main__":
    nums = [3, 2, 3]
    sol = Solution()
    print(sol.majorityElement(nums))
