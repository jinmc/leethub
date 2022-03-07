# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        
        runner1 = runner2 = dummy
        
        for _ in range(n+1):
            runner2 = runner2.next
        
        while runner2:
            runner1 = runner1.next
            runner2 = runner2.next
        
        runner1.next = runner1.next.next
        
        return dummy.next