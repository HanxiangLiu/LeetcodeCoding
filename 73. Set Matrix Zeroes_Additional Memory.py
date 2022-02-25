# Time complexity: O(MN)
# where M and N are the number of rows and columns respectively.
# Space Complexity O(M+N)
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        rows, cols, = set(), set()

        # Essentially, we mark the rows and columns that are to
        # be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and
        # cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol = Solution()
    sol.setZeroes(matrix=matrix)
    print(matrix)
