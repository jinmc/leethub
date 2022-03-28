"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, r):
        def trav(root):
            if not root.left and not root.right:
                return
            if not root.next:
                root.left.next = root.right
                root.right.next = None
            else:
                root.left.next = root.right
                root.right.next = root.next.left
            trav(root.left)
            trav(root.right)
        if not r:
            return
        # r.next = None
        trav(r)
        return r