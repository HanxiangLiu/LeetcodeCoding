# Time Complexity O(N), where N is the number of nodes in the BST.
# In the worst case we might be visiting all the nodes of the BST.
#
# Space Complexity O(1).
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


if __name__ == "__main__":
    nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root = TreeNode().genTree(nodes)
    p = TreeNode(2)
    q = TreeNode(8)
    sol = Solution()
    res = sol.lowestCommonAncestor(root, p, q)
    print(res.val)
