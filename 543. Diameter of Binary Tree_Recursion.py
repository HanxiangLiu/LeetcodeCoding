# Time Complexity O(N)
#
# Space Complexity O(N)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def genTree(self, arr: list[int]):
        def gen(arr: list[int], i: int) -> TreeNode:
            if i < len(arr):
                tn = TreeNode(arr[i]) if arr[i] is not None else None
                if tn is not None:
                    tn.left = gen(arr, 2 * i + 1)
                    tn.right = gen(arr, 2 * i + 2)
                return tn
        return gen(arr, 0)


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(root: TreeNode) -> int:
            nonlocal diameter
            if not root:
                return 0
            else:
                left_dia = depth(root.left)
                right_dia = depth(root.right)
                diameter = max(diameter, left_dia + right_dia)
                return max(left_dia, right_dia) + 1

        diameter = 0
        depth(root)
        return diameter


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    root = TreeNode().genTree(nodes)
    sol = Solution()
    res = sol.diameterOfBinaryTree(root)
    print(res)
