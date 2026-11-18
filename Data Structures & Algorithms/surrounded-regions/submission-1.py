class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        rows,cols=len(grid),len(grid[0])
        # capture unsurrounded regions O->T

        def capture(r,c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!="O"):
                return 
            grid[r][c]="T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j]=="O" and (i in [0,rows-1] or j in [0,cols-1])):
                    capture(i,j) 
        # now make all O to X and T->O
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="O":
                    grid[i][j]="X"
                if grid[i][j]=="T":
                    grid[i][j]="O"
        
        
