# Time complexity O(N).
# Because each node in the list is checked exactly once
# to determine if it is a duplicate or not, the total run
# time is O(N), where N is the number of nodes in the list.
#
# Space complexity O(1).
# No additional space is used.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev, curr = head, head.next if head else None
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head


if __name__ == "__main__":
    nodes = [1, 1, 2]
    head = ListNode(val=nodes[0])
    current = head
    for i in range(1, len(nodes)):
        current.next = ListNode(val=nodes[i])
        current = current.next
    sol = Solution()
    node = sol.deleteDuplicates(head=head)
    res = []
    while node is not None:
        res.append(node.val)
        node = node.next
    print(res)
