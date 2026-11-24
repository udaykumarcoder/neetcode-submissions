class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=collections.defaultdict(list)
        for i,eq in enumerate(equations):
            a,b=eq
            adj[a].append([b,values[i]])
            adj[b].append([a,1/values[i]])
        
        def bfs(q1,q2):
            if q1 not in adj or q2 not in adj:
                return -1
            
            q,visit=deque(),set()
            q.append([q1,1])
            visit.add(q1)
            while q:
                n,w=q.popleft()
                if n==q2:
                    return w
                for nei,weight in adj[n]:
                    if nei not in visit:
                        q.append([nei,w*weight])
                        visit.add(nei)
            return -1


        
        return [bfs(q[0],q[1]) for q in queries]