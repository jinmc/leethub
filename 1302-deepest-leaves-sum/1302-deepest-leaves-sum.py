# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        np_dict = defaultdict(int)
        
        def dfs(node_pair):
            n, node = node_pair
            np_dict[n] += node.val
            if node.left:
                dfs((n+1, node.left))
            if node.right:
                dfs((n+1, node.right))
        
        dfs((0, root))
        
        return max(np_dict.items(), key = lambda x: x[0])[1]