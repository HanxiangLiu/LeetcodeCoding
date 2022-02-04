# Time Complexity O(N)
# We iterate over nums once and make a constant time Hashmap insertion on each iteration.
# Therefore, the algorithm runs in O(N) time.
#
# Space Complexity O(N)
# At most, the HashMap can contain N-0.5N associations, so it occupies O(N) space. This
# is because an arbitrary array of length N can contain N distinct values, but nums is
# guaranteed to contain a majority element, which will occupy (at minimum) 0.5N+1 array
# indices. Therefore, N-(0.5N+1) indices can be occupied by distinct, non-majority
# elements (plus 1 for the majority element itself), leaving us with (at most) N-0.5N
# distinct elements.
import collections


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


if __name__ == "__main__":
    nums = [3, 2, 3]
    sol = Solution()
    print(sol.majorityElement(nums))
