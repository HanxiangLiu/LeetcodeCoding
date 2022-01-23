# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


if __name__ == "__main__":
    value = [3, 2, 0, -4]
    pos = 1
    nodes = [ListNode(0)] * len(value)
    for i, val in enumerate(value):
        nodes[i] = ListNode(val)
        try:
            nodes[i].next = nodes[i+1]
        except IndexError:
            nodes[i].next = nodes[pos]
    head = nodes[0]
    sol = Solution()
    print(sol.hasCycle(head=head))


