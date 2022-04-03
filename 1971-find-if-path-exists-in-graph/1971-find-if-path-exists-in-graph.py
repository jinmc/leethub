class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        stack = []
        vertex_set = set()
        stack.append(source)
        edge_dict = {i:set() for i in range(n)}
        for edge in edges:
            edge_dict[edge[0]].add(edge[1])
            edge_dict[edge[1]].add(edge[0])
        
        while stack:
            this_vertex = stack.pop()
            if destination in edge_dict[this_vertex]:
                return True
            vertex_set.add(this_vertex)
            
            for v in edge_dict[this_vertex]:
                if v not in vertex_set:
                    stack.append(v)
        return False