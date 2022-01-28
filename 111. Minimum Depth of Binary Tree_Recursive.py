# Time Complexity O(N). we visit each node exactly once.
#
# Space Complexity O(N).
# In the worst case, the tree is completely unbalanced, e.g. each node
# has only one child node, the recursion call would occur N times (the
# height of the tree), therefore the storage to keep the call stack
# would be O(N). But in the best case (the tree is completely balanced),
# the height of the tree would be log(N). Therefore, the space
# complexity in this case would be O(log(N)).
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
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        children = [root.left, root.right]
        # if we're at leaf node
        if not any(children):
            return 1

        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1


if __name__ == "__main__":
    nodes = [3, 9, 20, None, None, 15, 7]
    root = TreeNode().genTree(nodes)
    sol = Solution()
    res = sol.minDepth(root)
    print(res)
