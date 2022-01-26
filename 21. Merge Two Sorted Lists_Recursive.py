# Time Complexity O(N+M).
# Because each recursive call increments the pointer to list1 or list2 by one
# (approaching the dangling null at end of each list), there will be exactly one
# call to mergeTwoLists per element in each list. Therefore, the time complexity
# is linear in the combined size of the lists.
#
# Space Complexity O(N+M)
# The first call to mergeTwoLists does not return until the ends of both list1 and
# lsit2 have been reached, so N+M stack frames consume O(N+M) space.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


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