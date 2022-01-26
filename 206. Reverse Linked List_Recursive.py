# Time Complexity O(N).
# Assume that n is the list's length, the time complexity
# is O(N).
#
# Space complexity O(N).
# The extra space comes from implicit stack space due to
# recursion. The recursion could go up to n levels deep.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


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