# Time Complexity O(N), where N is a number of nodes in the tree,
# since one visits each node exactly once.
# Space Complexity O(N).
# O(logN) in the best case of completely balanced tree and
# O(N) in the worst case of completely unbalanced tree, to
# keep a recursion stack.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def genTree(self, arr: list[int]):
        def gen(arr: list[int], i: int) -> TreeNode:
            if i < len(arr):
                tn = TreeNode(arr[i]) if arr[i] else None
                if tn:
                    tn.left = gen(arr, 2 * i + 1)
                    tn.right = gen(arr, 2 * i + 2)
                return tn

        return gen(arr, 0)


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # q and p are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)


if __name__ == "__main__":
    node_p = [1, 2, 3]
    node_q = [1, 2, 3]
    p = TreeNode().genTree(node_p)
    q = TreeNode().genTree(node_q)
    sol = Solution()
    print(sol.isSameTree(p=p, q=q))
