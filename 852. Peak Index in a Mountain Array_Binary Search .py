# Time Complexity O(logN), where N is the length of arr.
#
# Space Complexity O(1).
class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if arr[mi] < arr[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo


if __name__ == "__main__":
    mountain = [0, 1, 0]
    sol = Solution()
    print(sol.peakIndexInMountainArray(arr=mountain))
