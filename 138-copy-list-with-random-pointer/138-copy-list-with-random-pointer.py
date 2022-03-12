"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        node_list = []
        run = head
        while run:
            node_list.append(run)
            run = run.next
        
        back_run = None
        new_node_list = []
        for i in range(len(node_list)-1, -1, -1):
            back_run = Node(node_list[i].val, back_run)
            new_node_list.insert(0, back_run)
        new_head = back_run
        
        for i in range(len(node_list)):
            if node_list[i].random is None:
                pass
            else:
                new_node_list[i].random = new_node_list[node_list.index(node_list[i].random)]
            
        
        return new_node_list[0]