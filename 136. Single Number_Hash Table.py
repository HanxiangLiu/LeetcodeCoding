# Time complexity O(n·1)=O(n). Time complexity of for loop is O(n).
# Time complexity of hash table (dictionary in python) operation pop
# is O(1)
#
# Space complexity O(n). The space required by hash_table is equal to
# the number of elements in nums.
import collections


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        hash_table = collections.defaultdict(int)
        # hash_table = {}
        # 使用defaultdict方法创建dict包含初始值，避免出现keyerror错误
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 1]
    print(sol.singleNumber(nums))
