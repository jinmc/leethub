# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # my_q = deque([(p, q)])
        my_q = [(p, q)]        
        while my_q:
            item = my_q.pop()
            p, q = item
            if p is None and q is None:
                pass
            elif p is None or q is None:
                return False
            elif p.val != q.val:
                return False
            else: # p.val == q.val
                my_q.append((p.left, q.left))
                my_q.append((p.right, q.right))
        return True
