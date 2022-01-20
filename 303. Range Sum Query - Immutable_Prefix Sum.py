# Time complexity O(1) time per query, O(n^2) time pre-computation.
#  Since the cumulative sum is cached, each sumRange query can be
#  calculated in O(1) time.

# Space complexity O(n)

# sumRange(i,j)=sum[j+1]−sum[i]
class NumArray:

    def __init__(self, nums: list[int]):
        # 这里1不能写在len()里面
        self.data = [0] * (len(nums)+1)
        for i in range(len(nums)):
            self.data[i+1] = self.data[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.data[right+1] - self.data[left]


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
