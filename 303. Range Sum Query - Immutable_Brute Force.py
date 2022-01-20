# Time complexity O(N). Each sumRange query takes O(N) time.

# Space complexity O(1). Note that data is a reference to nums and is
# not a copy of it.
class NumArray:

    def __init__(self, nums: list[int]):
        self.data = nums

    def sumRange(self, left: int, right: int) -> int:
        sum_na = 0
        for each in range(left, right+1):
            sum_na += self.data[each]
        return sum_na

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


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
