# Time complexity O(MN). This is because we visit each element once.
# Let M be the number of rows and N be the number of columns.
#
# Space Complexity O(1).
# This is because we don't use other data structures. Remember that we
# don't include the output array in the space complexity.
# range函数含前不含后
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right -1 , left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    result = sol.spiralOrder(matrix=matrix)
    print(result)
