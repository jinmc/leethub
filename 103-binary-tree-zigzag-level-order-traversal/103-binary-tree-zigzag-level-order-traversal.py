# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        my_dict = {}
        
        queue = [root]
        depth = 0
        while queue:
            q = list(queue)
            queue = []
            depth += 1
            for node in q:
                if not node:
                    continue
                if depth not in my_dict:
                    my_dict[depth] = [node.val]
                else:
                    my_dict[depth].append(node.val)
                queue.append(node.left)
                queue.append(node.right)
                
        print(my_dict)
        result = []
        for k, v in my_dict.items():
            if k % 2 != 0:
                result.append(v)
            else:
                result.append(reversed(v))
        return result
        
        