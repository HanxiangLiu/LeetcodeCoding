# Time complexity O(N).
# The whole tree is traversed once only. Here N refers to the total number of nodes
# in the given binary tree.
#
# Space Complexity O(N).
# we use a array with 2N elements. Besides, res and count array of size h are used.
# Here, h refers to the height(maximum number of levels
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
        info = []

        def dfs(node: TreeNode, depth=0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root)

        return [s/float(c) for s, c in info]


if __name__ == "__main__":
    nodes = [3, 9, 20, None, None, 15, 7]
    root = TreeNode().genTree(nodes)
    sol = Solution()
    res = sol.averageOfLevels(root)
    print(res)
