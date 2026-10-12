import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap=[-i for i in stones]
        heapq.heapify(self.heap)
        while len(self.heap)>1:
            x,y=heapq.heappop(self.heap),heapq.heappop(self.heap)
            x,y=-x,-y
            if x!=y and x<y:
                n=y-x
                heapq.heappush(self.heap,-n)
            elif x!=y and x>y:
                n=x-y
                heapq.heappush(self.heap,-n)
        return -self.heap[0] if self.heap else 0
