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
        if not root:
            return False
        return self.isSameTree(root, subRoot) or \
               self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            # q and p are both None
            if not p and not q:
                return True
            # one of p and q is None
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        stack = [(p, q), ]
        while stack:
            p, q = stack.pop()
            if not check(p, q):
                return False

            if p:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))

        return True


if __name__ == "__main__":
    nodes = [3, 4, 5, 1, 2]
    sub_nodes = [4, 1, 2]
    root = TreeNode().genTree(nodes)
    subRoot = TreeNode().genTree(sub_nodes)
    sol = Solution()
    res = sol.isSubtree(root, subRoot)
    print(res)
