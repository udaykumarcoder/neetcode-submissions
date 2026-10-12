import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks).values()
        q=deque()
        heap=[-i for i in count]
        heapq.heapify(heap)
        interval=0
        while heap or q:
            interval+=1
            if heap:
                cnt=1+heapq.heappop(heap)
                if cnt:
                    q.append((cnt,interval+n))
            if q and q[0][1]==interval:
                heapq.heappush(heap,q.popleft()[0])
        return interval