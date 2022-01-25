# Time Complexity O(N).
# Space Complexity O(N).
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        nextNode = self.removeElements(head=head.next, val=val)
        if head.val == val:
            return nextNode
        head.next = nextNode
        return head


if __name__ == "__main__":
    nodes = [1, 2, 6, 3, 4, 5, 6]
    val = 6
    head = ListNode(val=nodes[0])
    current = head
    for i in range(1, len(nodes)):
        current.next = ListNode(val=nodes[i])
        current = current.next
    sol = Solution()
    node = sol.removeElements(head=head, val=val)
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)
