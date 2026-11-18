class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        q=deque()
        time,fresh=0,0
        def addStep(r,c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!=1):
                return
            grid[r][c]=2
            q.append([r,c])
            nonlocal fresh
            fresh-=1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append([i,j])
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                addStep(r+1,c)
                addStep(r-1,c)
                addStep(r,c+1)
                addStep(r,c-1)
            time+=1
        return time if fresh==0 else -1