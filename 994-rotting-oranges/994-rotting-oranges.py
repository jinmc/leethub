from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        day = 0
        fresh_count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        while (queue or fresh_count == 0):
            if fresh_count == 0:
                return day
            new_queue = []
            for i, j in queue:
                for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:
                    new_i, new_j = i+di, j+dj
                    if 0 <=new_i < m and 0<=new_j<n:
                        if grid[new_i][new_j] == 1:
                            grid[new_i][new_j] = 2
                            fresh_count -= 1
                            new_queue.append((new_i, new_j))
            day += 1
            queue = new_queue
        return -1
                        
        
            
            