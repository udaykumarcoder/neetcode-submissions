class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visit=set()
        minheap=[[grid[0][0],0,0]] #maxheight/time ,r,c
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        visit.add((0,0))
        while minheap:
            t,r,c=heapq.heappop(minheap)
            if r==n-1 and c==n-1:
                return t
            for dr,dc in directions:
                newR,newC=r+dr,c+dc
                if (newR<0 or newC<0 or newR==n or newC==n or (newR,newC) in visit):
                    continue
                visit.add((newR,newC))
                heapq.heappush(minheap,[max(t,grid[newR][newC]),newR,newC])