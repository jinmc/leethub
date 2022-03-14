# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        dummy = ListNode(-1)
        run = dummy
        advance = head
        lst = []
        while advance:
            lst.append(run)
            if advance.next:
                temp = advance.next.next
                run.next = advance.next
                run = run.next
                run.next = advance
                run = run.next
                advance = temp
            else:
                run.next = advance
                run = run.next
                advance = advance.next
            run.next = None
        print(lst)
        return dummy.next