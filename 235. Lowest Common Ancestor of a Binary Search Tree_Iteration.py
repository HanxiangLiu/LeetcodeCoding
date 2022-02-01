# Time Complexity O(N), where N is the number of nodes in the BST.
# In the worst case we might be visiting all the nodes of the BST.
#
# Space Complexity O(N). This is because the maximum amount of space
# utilized by the recursion stack would be N since the height of a
# skewed BST could be N.
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
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node


if __name__ == "__main__":
    nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root = TreeNode().genTree(nodes)
    p = TreeNode(2)
    q = TreeNode(8)
    sol = Solution()
    res = sol.lowestCommonAncestor(root, p, q)
    print(res.val)
