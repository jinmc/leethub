# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        this_set = set()
        while head and head not in this_set:
            this_set.add(head)
            head = head.next
        
        if head in this_set:
            return True
        return False