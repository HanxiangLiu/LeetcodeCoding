# Time Complexity O(M + N), where M is the number of nodes in binary
# tree root, N is the number of nodes in binary tree subRoot.
#
# Space Complexity O(M + N)
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
        def serialize(root):
            if not root:
                return ",#"

            return "," + str(root.val) + serialize(root.left) + serialize(root.right)

        def getLPS(s):
            m, j = len(s), 0
            lps = [0] * m
            for i in range(1, m):
                while s[i] != s[j] and j > 0: j = lps[j - 1]
                if s[i] == s[j]:
                    j += 1
                    lps[i] = j
            return lps

        def kmp(s, p):
            lps = getLPS(p)
            n, m, j = len(s), len(p), 0
            for i in range(n):
                while s[i] != p[j] and j > 0: j = lps[j - 1]
                if s[i] == p[j]:
                    j += 1
                    if j == m: return True
            return False

        return kmp(serialize(root), serialize(subRoot))


if __name__ == "__main__":
    nodes = [3, 4, 5, 1, 2]
    sub_nodes = [4, 1, 2]
    root = TreeNode().genTree(nodes)
    subRoot = TreeNode().genTree(sub_nodes)
    sol = Solution()
    res = sol.isSubtree(root, subRoot)
    print(res)
