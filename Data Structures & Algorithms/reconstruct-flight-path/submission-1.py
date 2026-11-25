class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        # Sort in reverse so we can pop the smallest destination from the end in O(1)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        route = []

        def dfs(airport: str) -> None:
            while adj[airport]:
                nxt = adj[airport].pop()
                dfs(nxt)
            route.append(airport)

        dfs("JFK")
        return route[::-1]