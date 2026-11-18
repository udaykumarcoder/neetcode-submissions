class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        q=deque()
        visit=set()

        def addStep(r,c):
            if ( r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==-1 or (r,c) in visit):
                return
            visit.add((r,c))
            q.append([r,c])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append([i,j])
                    visit.add((i,j))
        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                addStep(r+1,c)
                addStep(r-1,c)
                addStep(r,c+1)
                addStep(r,c-1)
            dist+=1