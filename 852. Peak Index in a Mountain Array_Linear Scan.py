# Time Complexity O(N), where N is the length of arr.
#
# Space Complexity O(1).
class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        for i in range(len(arr)):
            if arr[i] > arr[i+1]:
                return i


if __name__ == "__main__":
    mountain = [0, 1, 0]
    sol = Solution()
    print(sol.peakIndexInMountainArray(arr=mountain))
