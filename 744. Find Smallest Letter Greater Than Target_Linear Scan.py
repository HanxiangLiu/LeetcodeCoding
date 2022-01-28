# Time Complexity O(N), where N is the length of letters. We scan
# every element of the array.
#
# Space Complexity O(1), as we maintain only pointers
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c
        return letters[0]


if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "a"
    sol = Solution()
    print(sol.nextGreatestLetter(letters=letters, target=target))
