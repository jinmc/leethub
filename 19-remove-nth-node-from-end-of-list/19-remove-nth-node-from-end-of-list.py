# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 공통
        dummy = ListNode(-1)
        dummy.next = head
        
        r1 = r2 = dummy
        
        for _ in range(n+1):
            r2 = r2.next
            
        # r2가 none
        while r2:
            r1 = r1.next
            r2 = r2.next
        
        r1.next = r1.next.next
        
        return dummy.next
        