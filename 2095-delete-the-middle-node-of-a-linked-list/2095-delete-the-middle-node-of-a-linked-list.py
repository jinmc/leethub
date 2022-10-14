# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        dummy = ListNode(-1, head)
        
        num = 0
        while temp:
            num += 1
            temp = temp.next
        # print(num)
        
        mid_idx = num // 2
        
        temp_dummy = dummy
        num = 0
        while temp_dummy:
            if num == mid_idx:
                temp_dummy.next = temp_dummy.next.next
                break
            num += 1
            temp_dummy = temp_dummy.next
        
        return dummy.next