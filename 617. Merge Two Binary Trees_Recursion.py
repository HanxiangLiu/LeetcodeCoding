# Time Complexity O(N). A total of N nodes need to be traversed. Here, N represents
# the minimum number of nodes from the two given trees.
#
# Space Complexity O(N). The depth of the recursion tree can go upto N in the case
# of a skewed tree. In average case, depth will be O(logN)
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
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            res = TreeNode(root1.val + root2.val)
            res.left = self.mergeTrees(root1.left, root2.left)
            res.right = self.mergeTrees(root1.right, root2.right)
        return res


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

