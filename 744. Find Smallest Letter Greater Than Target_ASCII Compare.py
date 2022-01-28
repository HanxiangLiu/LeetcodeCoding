# Time Complexity O(N), where N is the length of letters. We scan
# every element of the array.
#
# Space Complexity O(1), the maximum size of seen
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        seen = set(letters)
        for i in range(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand


if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "a"
    sol = Solution()
    print(sol.nextGreatestLetter(letters=letters, target=target))
