# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        run = head
        prev = dummy
        # run 노드랑 prev 노드
        while run:
            if run.next and run.next.val == run.val:
                while run.next and run.next.val == run.val:
                    run = run.next
                prev.next = run.next
            else:
                prev = prev.next
            run = run.next
            
        return dummy.next