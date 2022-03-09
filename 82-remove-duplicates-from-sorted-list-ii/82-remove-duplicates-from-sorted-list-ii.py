# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        this_set = set()
        dup_set = set()
        run = head
        while run:
            if run.val in this_set:
                dup_set.add(run.val)
            else:
                this_set.add(run.val)
            run = run.next
                
        dummy = ListNode(-1)
        dummy.next = head
        r1 = dummy
        while r1:
            if r1.next and r1.next.val in dup_set:
                r1.next = r1.next.next
            else:
                r1 = r1.next
            
        return dummy.next
            
                
        