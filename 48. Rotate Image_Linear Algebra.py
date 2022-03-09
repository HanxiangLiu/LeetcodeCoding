# Time Complexity O(N), N is the number of cells in the matrix.
# We perform two steps: transposing the matrix, and then reversing each row.
# Transposing the matrix has a cost of O(N) because we're moving the value of
# each cell once. Reversing each row also has a cost of O(N), because again
# we're moving the value of each cell once.
#
# Space Complexity O(1), because we do not use any other additional
# data structures.
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)

    @staticmethod
    def transpose(m):
        n = len(m)
        for i in range(n):
            for j in range(i + 1, n):
                m[j][i], m[i][j] = m[i][j], m[j][i]

    @staticmethod
    def reflect(m):
        n = len(m)
        for i in range(n):
            for j in range(n // 2):
                m[i][j], m[i][-j - 1] = m[i][-j - 1], m[i][j]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    sol.rotate(matrix=matrix)
    print(matrix)
