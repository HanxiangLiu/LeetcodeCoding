# Time Complexity O(N).
# Assume that n is the list's length, the time complexity
# is O(N).
#
# Space complexity O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr is not None:
            curr.next, prev, curr = prev, curr, curr.next
        return prev


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    head = ListNode(nodes[0])
    current = head
    for i in range(1, len(nodes)):
        current.next = ListNode(nodes[i])
        current = current.next
    sol = Solution()
    node = sol.reverseList(head)
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)