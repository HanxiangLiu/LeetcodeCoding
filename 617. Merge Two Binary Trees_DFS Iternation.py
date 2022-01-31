# Time Complexity O(N). We traverse over a total of N nodes.
# Here, N refers to the smaller of the number of nodes in the two trees.
#
# Space Complexity O(N). The depth of stack can grow upto N in
# case of a skewed tree.
import copy


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
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not (root1 and root2):
            return root1 or root2

        mer = copy.deepcopy(root1)
        stack = [(mer, root1, root2), ]
        while stack:
            r0, r1, r2 = stack.pop()
            if not r1 or not r2:
                continue
            r0.val = r1.val + r2.val

            if not r1.left:
                r0.left = r2.left
            else:
                stack.append((r0.left, r1.left, r2.left))

            if not r1.right:
                r0.right = r2.right
            else:
                stack.append((r0.right, r1.right, r2.right))
        return mer


if __name__ == "__main__":
    root1 = [1, 3, 2, 5]
    root2 = [2, 1, 3, None, 4, None, 7]
    r1 = TreeNode().genTree(root1)
    r2 = TreeNode().genTree(root2)
    sol = Solution()
    mer = sol.mergeTrees(root1=r1, root2=r2)
    nodes, res = [mer, ], []
    while nodes:
        for _ in range(len(nodes)):
            node = nodes.pop(0)
            res.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
    print(res)

