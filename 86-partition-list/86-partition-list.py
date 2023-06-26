# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:


  
       
        smaller_head = ListNode(0)
        greater_head = ListNode(0)
        smaller_ptr = smaller_head
        greater_ptr = greater_head
       
        while head:
            if head.val < x:
              
                smaller_ptr.next = head
                smaller_ptr = smaller_ptr.next
            else:
               
                greater_ptr.next = head
                greater_ptr = greater_ptr.next

            head = head.next

        greater_ptr.next = None
        smaller_ptr.next = greater_head.next

        return smaller_head.next
