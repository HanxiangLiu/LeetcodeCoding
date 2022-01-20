# Time complexity O(1) time per query, O(n^2) time pre-computation.
# The pre-computation done in the constructor takes O(n^2) time.
# Each sumRange query's time complexity is O(1) as the hash table's
# look up operation is constant time.

# Space complexity O(n^2) The extra space required is O(n^2) as
# there are n candidates for both i and j.

# We could trade in extra space for speed. By pre-computing all range
# sum possibilities and store its results in a hash table, we can
# speed up the query to constant time.
class NumArray:

    def __init__(self, nums: list[int]):
        self.dataMap = {}
        for i in range(len(nums)):
            sum_data = 0
            for j in range(i, len(nums)):
                sum_data += nums[j]
                # 列表的值是可变的，不能作为字典的键；元组的值是不可变的，可以作为字典的键
                self.dataMap[(i, j)] = sum_data

    def sumRange(self, left: int, right: int) -> int:
        return self.dataMap[(left, right)]


if __name__ == "__main__":
    order = ["NumArray", "sumRange", "sumRange", "sumRange"]
    nums = [[-2, 0, 3, -5, 2, -1], [0, 2], [2, 5], [0, 5]]
    result = []
    for i in range(len(order)):
        if order[i] == "NumArray":
            na = NumArray(nums[i])
            result.append(None)
        elif order[i] == "sumRange":
            sumNA = na.sumRange(left=nums[i][0], right=nums[i][1])
            result.append(sumNA)
    print(result)
