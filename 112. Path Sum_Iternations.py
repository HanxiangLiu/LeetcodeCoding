# Time Complexity O(N), where N is the number of nodes
# We visit node exactly once.
#
# Space Complexity O(N).
#  since in the worst case, when the tree is completely unbalanced,
#  e.g. each node has only one child node, we would keep all N
#  nodes in the stack. But in the best case (the tree is balanced),
#  the height of the tree would be log(N). Therefore, the space
#  complexity in this case would be O(log(N)).
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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val), ]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
        return False


if __name__ == "__main__":
    nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    target = 22
    root = TreeNode().genTree(nodes)
    sol = Solution()
    print(sol.hasPathSum(root=root, targetSum=target))
