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
    head = ListNode(value[0])
    current = head
    for i in range(1, len(value)):
        current.next = ListNode(value[i])
        current = current.next
    current.next = head.next
    sol = Solution()
    print(sol.hasCycle(head=head))


