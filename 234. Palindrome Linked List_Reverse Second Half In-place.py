# Time complexity O(N), where n is the number of nodes in the Linked List.
# Finding the middle is O(N), reversing a list in place is O(N), and
# then comparing the 2 resulting Linked Lists is also O(N).
#
# Space complexity O(1).
# We are changing the next pointers for half of the nodes. This was
# all memory that had already been allocated, so we are not using any
# extra memory and therefore it is O(1).

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


if __name__ == "__main__":
    nodes = [1, 2, 2, 1]
    head = ListNode(val=nodes[0])
    current = head
    for i in range(1, len(nodes)):
        current.next = ListNode(val=nodes[i])
        current = current.next
    sol = Solution()
    print(sol.isPalindrome(head=head))