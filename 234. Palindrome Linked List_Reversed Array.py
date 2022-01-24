# Time complexity O(n), where n is the number of nodes in the
# Linked List.
# In the first part, we're coping a Linked List into an Array List.
# Iterating down a Linked List in sequential order is O(N), and each
# of the N writes to the Array List is O(1). Therefore, the overall
# cost is O(N).
# In the second part, we're using Python trick(reverse and list
# comparison as a one liner), it costs O(N)
# This gives O(2N) = O(N) because we always drop the constants.
#
# Space complexity O(N), where n is the number of nodes in the
# Linked List. We are making an Array List and adding n values to it.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


if __name__ == "__main__":
    nodes = [1, 2, 2, 1]
    head = ListNode(val=nodes[0])
    current = head
    for i in range(1, len(nodes)):
        current.next = ListNode(val=nodes[i])
        current = current.next
    sol = Solution()
    print(sol.isPalindrome(head=head))
