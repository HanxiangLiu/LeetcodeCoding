# Time Complexity O(M + N),
# where M,N are the lengths of S and T respectively.
#
# Space Complexity O(M + N)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(str):
            ans = []
            for c in str:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)


if __name__ == "__main__":
    s = "ab#c"
    t = "ad#c"
    sol = Solution()
    print(sol.backspaceCompare(s, t))
