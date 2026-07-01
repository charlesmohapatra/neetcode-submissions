class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        queue.append((0,0))
        if grid[0][0] == 1:
            return -1
        visit = set()
        visit.add((0,0))
        length = 1
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == rows-1 and c == cols-1:
                    return length
                neighbours = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
                for dr, dc in neighbours:
                    if min((r+dr), (c+dc)) < 0 or r+dr == rows or c+dc == cols or grid[r+dr][c+dc] == 1 or (r+dr, c+dc) in visit:
                        continue
                    visit.add((r+dr, c+dc))
                    queue.append((r+dr, c+dc))
            length += 1
        return -1