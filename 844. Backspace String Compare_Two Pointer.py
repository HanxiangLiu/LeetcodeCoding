# Time Complexity O(M + N),
# where M,N are the lengths of S and T respectively.
#
# Space Complexity O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        rs = len(s) - 1
        rt = len(t) - 1

        while rs >= 0 or rt >= 0:
            chars = chart = ""
            if rs >= 0:
                chars, rs = self.getchar(s, rs)
            if rt >= 0:
                chart, rt = self.getchar(t, rt)
            if chars != chart:
                return False
        return True

    def getchar(self, str, r):
        char, skip = '', 0
        while r >= 0 and not char:
            if str[r] == '#':
                skip += 1
            elif skip == 0:
                char = str[r]
            else:
                skip -= 1
            r -= 1
        return char, r


if __name__ == "__main__":
    s = "ab#c"
    t = "ad#c"
    sol = Solution()
    print(sol.backspaceCompare(s, t))
