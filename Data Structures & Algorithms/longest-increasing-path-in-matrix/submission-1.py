class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        dp={}
        def dfs(r,c,prevVal):
            if (r==rows or c==cols or r<0 or c<0 or prevVal>=matrix[r][c]):
                return 0
            if (r,c,prevVal) in dp:
                return dp[(r,c,prevVal)]
            res=1
            res=max(res,1+dfs(r+1,c,matrix[r][c]))
            res=max(res,1+dfs(r-1,c,matrix[r][c]))
            res=max(res,1+dfs(r,c+1,matrix[r][c]))
            res=max(res,1+dfs(r,c-1,matrix[r][c]))
            dp[(r,c,prevVal)]=res
            return res
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,-1)
        return max(dp.values())