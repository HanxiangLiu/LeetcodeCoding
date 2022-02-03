# Time Complexity O(N)
# We visit each node in the tree only once. We cannot do better
# than that, since at the very least we have to visit each node
# to invert it.
#
# Space Complexity O(N).
# O(H) function calls wll be placed on the stack in the worst
# case, where H is the height of the tree. and h \in O(N)
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        stack = [root, ]
        while stack:
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return root


if __name__ == "__main__":
    nodes = [4, 2, 7, 1, 3, 6, 9]
    root = TreeNode().genTree(nodes)
    sol = Solution()
    inv_root = sol.invertTree(root)
    que, res = [inv_root, ], []
    while que:
        node = que.pop(0)
        res.append(node.val)
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    print(res)
