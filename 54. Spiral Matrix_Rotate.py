# Time complexity O(MN). This is because we visit each element once.
# Space Complexity O(1).
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    result = sol.spiralOrder(matrix=matrix)
    print(result)

#   spiral_order([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
#
#   = [1, 2, 3] + spiral_order([[6, 9],
#                             [5, 8],
#                             [4, 7]])
#
#   = [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
#                                      [5, 4]])
#
#   = [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
#                                               [5]])
#
#   = [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])
#
#   = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])
#
#   = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []
#
#   = [1, 2, 3, 6, 9, 8, 7, 4, 5]
