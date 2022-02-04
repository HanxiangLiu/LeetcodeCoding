
class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        ans = []
        if len(original) == m*n:
            for i in range(0, len(original), n):
                ans.append(original[i:i+n])
        return ans


if __name__ == "__main__":
    original = [1, 2, 3, 4]
    m, n = 2, 2
    sol = Solution()
    print(sol.construct2DArray(original, m, n))
