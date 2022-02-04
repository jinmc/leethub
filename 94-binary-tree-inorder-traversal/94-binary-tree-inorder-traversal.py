# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []
        node = root
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            # node = None
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result