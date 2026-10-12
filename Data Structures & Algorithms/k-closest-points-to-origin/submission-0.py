import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap=[]
        self.k=k
        self.cal=[]
        for i in points:
            dis=i[0]**(2)+i[1]**(2)
            self.cal.append((dis,i))
        for i in self.cal:
            heapq.heappush(self.heap,i)
        res=[]
        for _ in range(self.k):
            res.append(heapq.heappop(self.heap))        
        return [i[1] for i in res]