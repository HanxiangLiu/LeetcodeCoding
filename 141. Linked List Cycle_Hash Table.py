# Time Complexity O(n).
# We visit each of the n elements in the list at most once.
# Adding a node to the hash table costs only O(1) time.
#
# Space complexity O(n)
#  The space depends on the number of elements added to the
#  hash table, which contains at most n elements.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False


if __name__ == "__main__":
    value = [3, 2, 0, -4]
    pos = 1
    head = ListNode(value[0])
    current = head
    for i in range(1, len(value)-1):
        current.next = ListNode(value[i])
        current = current.next
    current.next = head.next
    sol = Solution()
    print(sol.hasCycle(head=head))


