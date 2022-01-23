# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def helper(root):
            if root.left:
                helper(root.left)
            result.append(root.val)
            if root.right:
                helper(root.right)
                
        if not root:
            return []
        helper(root)
        return result
        