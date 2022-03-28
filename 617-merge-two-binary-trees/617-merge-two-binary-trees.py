# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1, t2):
        """
        """
        if t1 is None:
            return t2
						
        stack = []
        stack.append((t1,t2))
        while stack:
            t = stack.pop()
            if t[1] is None:
                continue
            t[0].val += t[1].val
            
            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left,t[1].left))
            
            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right,t[1].right))
        return t1