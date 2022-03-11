# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None or head.next is None:
            return head
        
        run = head
        main_sum = 0
        while run:
            run = run.next
            main_sum += 1
        print(f'main sum : {main_sum}')
        k = k % main_sum
        if k == 0 or head is None or head.next is None:
            return head
        remain = main_sum - k
        real_head = head
        this_head = None
        
        cnt = 0
        while head:
            cnt += 1
            # head = head.next
            if head.next is None:
                head.next = real_head
                head = None
            elif cnt == remain:
                temp = head.next
                head.next = None
                head = temp
                this_head = temp
            else:    
                head = head.next
        return this_head
             