# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        runner = head
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    runner.next = list1
                    list1 = list1.next
                else:
                    runner.next = list2
                    list2 = list2.next
            else:
                this_node = list1 or list2
                runner.next = this_node
                if list1:
                    list1 = list1.next
                if list2:
                    list2 = list2.next
                this_node = this_node.next
            runner = runner.next
        return head.next