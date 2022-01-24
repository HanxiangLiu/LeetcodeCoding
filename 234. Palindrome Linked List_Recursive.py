# Time Complexity O(N), where N is the number of nodes in the Linked List.
# The recursive function is run once for each of the N nodes, and
# the body of the recursive function is O(1). Therefore, this gives
# a total of O(N).
#
# Space Complexity O(N), where n is the number of nodes in the Linked List.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer = head

        def recursively_check(current_node: ListNode) -> bool:
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check(head)


if __name__ == "__main__":
    nodes = [1, 2, 2, 1]
    head = ListNode(val=nodes[0])
    current = head
    for i in range(1, len(nodes)):
        current.next = ListNode(val=nodes[i])
        current = current.next
    sol = Solution()
    print(sol.isPalindrome(head=head))

# Each time a function is called within a function, the computer
# needs to keep track of where it is up to (and the values of any
# local variables) in the current function before it goes into the
# called function. It does this by putting an entry on something
# called the runtime stack, called a stack frame. Once it has created
# a stack frame for the current function, it can then go into the
# called function. Then once it is finished with the called function,
# it pops the top stack frame to resume the function it had been in
# before the function call was made.
# Before doing any palindrome checking, the above recursive function
# creates nn of these stack frames because the first step of
# processing a node is to process the nodes after it, which is done
# with a recursive call. Then once it has the nn stack frames, it
# pops them off one-by-one to process them.
# So, the space usage is on the runtime stack because we are creating
# n stack frames. Always make sure to consider what's going on the
# runtime stack when analyzing a recursive function. It's a common
# mistake to forget to.
# Not only is this approach still using O(n)O(n) space, it is worse
# than the first approach because in many languages (such as Python),
# stack frames are large, and there's a maximum runtime stack depth
# of 1000 (you can increase it, but you risk causing memory errors
# with the underlying interpreter). With every node creating a stack
# frame, this will greatly limit the maximum Linked List size the
# algorithm can handle.
