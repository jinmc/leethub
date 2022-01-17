# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        runnerNode = dummyNode
        leftover = 0
        while l1 is not None or l2 is not None or leftover > 0:
            if l1 is None and l2 is None and leftover == 1:
                runnerNode.next = ListNode(val = 1)
                leftover = 0
            elif l1 is None:
                if leftover + l2.val >=10:
                    runnerNode.next = ListNode(val = leftover + l2.val - 10)
                    leftover = 1
                else:
                    runnerNode.next = ListNode(val = leftover + l2.val)
                    leftover = 0
                l2 = l2.next
            elif l2 is None:
                if leftover + l1.val >= 10:
                    runnerNode.next = ListNode(val = leftover + l1.val - 10)
                    leftover = 1
                else:
                    runnerNode.next = ListNode(val = leftover + l1.val)
                    leftover = 0
                l1 = l1.next
            else:
                if leftover + l1.val + l2.val >= 10:
                    runnerNode.next = ListNode(val= leftover + l1.val + l2.val - 10)
                    leftover = 1
                else:
                    runnerNode.next = ListNode(val=leftover + l1.val + l2.val)
                    leftover = 0
                l1 = l1.next
                l2 = l2.next
            runnerNode = runnerNode.next
        return dummyNode.next