import numpy


class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) == m*n:
            return numpy.reshape(original, (m, n)).tolist()
        return []


if __name__ == "__main__":
    original = [1, 2, 3, 4]
    m, n = 2, 2
    sol = Solution()
    print(sol.construct2DArray(original, m, n))
