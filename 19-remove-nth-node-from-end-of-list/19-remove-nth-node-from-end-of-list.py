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
        
        # 노드 숫자 세기
        cnt = 0
        runner = head
        while runner:
            runner = runner.next
            cnt += 1
            
        # 몇번째 에서 뺄지 정함
        cnt -= n
        this_cnt = 0
        runner = dummy
        
        while runner:
            if this_cnt == cnt:
                runner.next = runner.next.next
                break
            this_cnt += 1
            runner = runner.next
            
                
        return dummy.next