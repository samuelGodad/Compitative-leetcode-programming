# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create dummy head to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy

        # Move p2 n steps ahead of p1
        for i in range(n):
            p2 = p2.next

        # Move both pointers until p2 reaches the end of the list
        while p2.next:
            p1 = p1.next
            p2 = p2.next

        # Remove the nth node from the end
        p1.next = p1.next.next

        return dummy.next  