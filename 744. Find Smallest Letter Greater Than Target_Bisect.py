# Time Complexity O(logN), where N is the length of letters. We scan
# only log N elements of the array.
#
# Space Complexity O(1), as we maintain only pointers
import bisect


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]


if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "a"
    sol = Solution()
    print(sol.nextGreatestLetter(letters=letters, target=target))
