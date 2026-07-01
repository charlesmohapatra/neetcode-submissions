class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visit = set()
        visit_0 = set()
        fresh_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visit.add((i,j))
                elif grid[i][j] == 0:
                    visit_0.add((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        if len(queue) == 0:
            return -1
        timer = -1
        while len(queue):
            for i in range(len(queue)):
                r,c = queue.popleft()
                neighbours = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in neighbours:
                    if r+dr < 0 or c+dc < 0 or r+dr == rows or c+dc == cols or (r+dr, c+dc) in visit:
                        continue
                    elif grid[r+dr][c+dc] == 0:
                        visit_0.add((r+dr, c+dc))
                        continue
                    queue.append((r+dr, c+dc))
                    visit.add((r+dr, c+dc))
            timer += 1
        if len(visit) + len(visit_0) == rows * cols:
            return timer
        else:
            return -1