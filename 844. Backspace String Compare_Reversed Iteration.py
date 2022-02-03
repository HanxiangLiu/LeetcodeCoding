# Time Complexity O(M + N),
# where M,N are the lengths of S and T respectively.
#
# Space Complexity O(1)
import itertools


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in
                   itertools.zip_longest(F(S=s), F(S=t)))


if __name__ == "__main__":
    s = "ab#c"
    t = "ad#c"
    sol = Solution()
    print(sol.backspaceCompare(s, t))
