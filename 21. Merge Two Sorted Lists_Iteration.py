# Time Complexity O(N+M).
# Because exactly one of list1 and list2 is incremented on each loop iteration,
# the while loop runs for a number of iterations equal to the sum of
# the lengths of the two lists. All other work is constant, so the
# overall complexity is linear.
#
# Space complexity O(1).
# The iterative approach only allocates a few pointers, so it has a
# constant overall memory footprint.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        # At least one of list1 and list2 can still have nodes at this point,
        # so connect the non-null list to the end of the merged list.
        prev.next = list1 or list2
        return prehead.next


if __name__ == "__main__":
    nodes1 = [1, 2, 4]
    nodes2 = [1, 3, 4]
    list1 = ListNode(nodes1[0])
    list2 = ListNode(nodes2[0])
    current = list1
    for i in range(1, len(nodes1)):
        current.next = ListNode(nodes1[i])
        current = current.next
    current = list2
    for j in range(1, len(nodes2)):
        current.next = ListNode(nodes2[j])
        current = current.next
    sol = Solution()
    node = sol.mergeTwoLists(list1, list2)
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)