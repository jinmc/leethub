# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        nodelist = [dummy]
        while head:
            nodelist.append(head)
            head = head.next
        target = len(nodelist) - n - 1
        nodelist[target].next = nodelist[target].next.next
        return dummy.next
        
