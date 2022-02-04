
class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        return [ original[i*n:(i+1)*n] for i in range(m) ] if len(original) == m*n else []


if __name__ == "__main__":
    original = [1, 2, 3, 4]
    m, n = 2, 2
    sol = Solution()
    print(sol.construct2DArray(original, m, n))
