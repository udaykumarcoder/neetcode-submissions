class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()
        row,col=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=row or j>=col or \
            grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            perim=dfs(i,j+1)
            perim+=dfs(i,j-1)
            perim+=dfs(i+1,j)
            perim+=dfs(i-1,j)
            return perim
        
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return dfs(i,j)