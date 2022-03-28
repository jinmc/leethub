# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## 5 % 2 = 2 [1,2,3,4,5]
## 4 % 2 = 2 [1,2,3,4]
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0 
        new_head = head
        while new_head != None:
            count += 1
            new_head = new_head.next
        # print(count)
        
        target = count // 2
        new_count = 0
        
        while new_count != target:
            head = head.next
            new_count += 1
            
        return head