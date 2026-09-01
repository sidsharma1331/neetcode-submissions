class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visits = set()
        def addcell(r,c):
            if r in range(rows) and c in range(cols) and (r,c) not in visits and grid[r][c]!=-1:
                q.append((r,c))
                visits.add((r,c))
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i,j))
                    visits.add((i, j))
        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                
                addcell(row+1,col)
                addcell(row-1,col)
                addcell(row,col+1)
                addcell(row,col-1)
            dist+=1

            

        