# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        while runner:
            if runner.next and runner.val == runner.next.val:
                runner.next = runner.next.next
            else:
                runner = runner.next     
        return head