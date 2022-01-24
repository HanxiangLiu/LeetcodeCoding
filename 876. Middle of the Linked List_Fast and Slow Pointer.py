# Time Complexity O(N), where N is the number of nodes in the
# given list.
#
# Space Complexity O(1), the space used by slow and fast.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    value = [1, 2, 3, 4, 5]
    head = ListNode(value[0])
    current = head
    for i in range(1, len(value)):
        current.next = ListNode(value[i])
        current = current.next
    sol = Solution()
    res = sol.middleNode(head=head)
    output = []
    while res:
        output.append(res.val)
        res = res.next
    print(output)
