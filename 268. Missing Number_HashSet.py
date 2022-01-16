# Time complexity O(n).
# Because the set allows for O(1) containment queries, the
# main loop runs in O(n) time. Creating num_set costs O(n)
# time, as each set insertion runs in amortized O(1) time, so the
# overall runtime is O(n+n)=O(n). and the entire runtime is O(nlgn).
#
# Space complexity O(n)
# nums contains n-1 distinct elements, so it costs O(n)
# space to store a set containing all of them.
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        numSet = set(nums)
        for i in range(len(nums)+1):  # add 1 cause n=len(nums)+1
            if i not in numSet:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 0, 1]
    print(sol.missingNumber(nums=nums))
