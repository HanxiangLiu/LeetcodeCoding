# Time Complexity O(N). It's one pass solution.
#
# Space Complexity O(1). It's a constant space solution.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next


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

# 问题的核心在于如何处理删除首节点的情况，使用哨兵节点来解决这一问题
# In order  to save the need to treat the "head" as special,
# This algorithm uses a sentinel node. This simplifies the
# code greatly, particularly in the case of needing to
# remove the head AND some of the nodes immediately after
# it.
