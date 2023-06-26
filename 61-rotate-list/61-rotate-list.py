# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head
        
      
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        
     
        k %= length
        
     
        if k == 0:
            return head
        
     
        slow = fast = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        
      
        new_head = slow.next
        slow.next = None
        curr.next = head
        
        return new_head

        