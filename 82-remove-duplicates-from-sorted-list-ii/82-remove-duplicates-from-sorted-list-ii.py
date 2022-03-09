# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        
        pred = dummy
        run = head
        while run:
            
            if run.next and run.next.val == run.val:
                while run.next and run.val == run.next.val:
                    run = run.next
                pred.next = run.next
            else:
                pred = pred.next
            
            run = run.next
            # print(pred, run)
            
        
        return dummy.next