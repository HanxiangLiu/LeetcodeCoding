# Time complexity O(NLogN).
# The time complexity is dominated by sorting. Once the array has been sorted,
# only O(n) time is taken to go through the array and determine if there is any
# overlap.
# Space complexity O(1).
# No additional space is used.
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    sol = Solution()
    print(sol.canAttendMeetings(intervals))
