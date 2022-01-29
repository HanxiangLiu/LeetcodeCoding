# Time Complexity O(N). we visit each node exactly once.
#
# Space Complexity O(N). In the worst case we could keep up
# to the entire tree.
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
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue, max_depth = [(1, root), ], float('-inf')
        while queue:
            depth, root = queue.pop(0)
            children = [root.left, root.right]
            if not any(children):
                max_depth = max(depth, max_depth)
            for c in children:
                if c:
                    queue.append((depth + 1, c))
        return max_depth


if __name__ == "__main__":
    nodes = [3, 9, 20, None, None, 15, 7]
    root = TreeNode().genTree(nodes)
    sol = Solution()
    res = sol.maxDepth(root)
    print(res)
