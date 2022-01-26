# Time complexity O(N^2).
# Because we have two check every meeting with every other meeting
# Space complexity O(1).
# No additional space is used.
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        def overlap(interval1: list[int], interval2: list[int]) -> bool:
            return (
                    min(interval1[1], interval2[1]) >
                    max(interval1[0], interval2[0])
            )

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if overlap(intervals[i], intervals[j]):
                    return False
        return True


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    sol = Solution()
    print(sol.canAttendMeetings(intervals))
