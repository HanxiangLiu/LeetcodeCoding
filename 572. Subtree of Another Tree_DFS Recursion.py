# Time Complexity O(M * N), where M is the number of nodes in binary
# tree root, N is the number of nodes in binary tree subRoot.
#
# Space Complexity O(N), where n is the nodes of binary tree root.
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
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isEqual(root1, root2):
            if not (root1 and root2):
                return root1 == root2
            return root1.val == root2.val and \
                   isEqual(root1.left, root2.left) and \
                   isEqual(root1.right, root2.right)

        def dfs(root, subRoot):
            if not root:
                return False
            return isEqual(root, subRoot) or \
                   dfs(root.left, subRoot) or \
                   dfs(root.right, subRoot)

        return dfs(root, subRoot)


if __name__ == "__main__":
    nodes = [3, 4, 5, 1, 2]
    sub_nodes = [4, 1, 2]
    root = TreeNode().genTree(nodes)
    subRoot = TreeNode().genTree(sub_nodes)
    sol = Solution()
    res = sol.isSubtree(root, subRoot)
    print(res)
