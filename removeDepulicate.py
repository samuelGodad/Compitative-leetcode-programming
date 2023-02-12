# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

   
        if head is not None and head.next is not None:
            prev = None
            cur = head
            nex = head.next
            dup = None
            while nex is not None:
                if cur.val == nex.val:
                    dup = cur.val
                    while nex is not None and nex.val == dup:
                        nex = nex.next
                    if prev is None:
                        head = nex
                    else:
                        prev.next = nex
                else:
                    prev = cur
                cur = nex
                if nex is not None:
                    nex = nex.next
        return head
