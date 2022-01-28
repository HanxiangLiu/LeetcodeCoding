# Time complexity O(N).
#  The whole tree is traversed at most once. Here, n refers to the
#  number of nodes in the given binary tree.
#
# Space Complexity O(M).
# The size of queue or temp can grow upto at most the maximum number
# of nodes at any level in the given binary tree. Here, m refers
# to the maximum number of nodes at any level in the input tree.
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
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        if not root:
            return []
        nodes, res = [root, ], []
        while nodes:
            size, s = len(nodes), 0
            for _ in range(size):
                node = nodes.pop(0)
                s += node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            res.append(s/float(size))
        return res


if __name__ == "__main__":
    nodes = [3, 9, 20, None, None, 15, 7]
    root = TreeNode().genTree(nodes)
    sol = Solution()
    res = sol.averageOfLevels(root)
    print(res)
