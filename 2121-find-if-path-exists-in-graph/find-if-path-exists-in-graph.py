class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        seen = [False] * n
        seen[source] = True 

        q = deque([source])

        while q:
            u = q.popleft()
            if u == destination:
                return True
            for v in g[u]:
                if not seen[v]:
                    seen[v] = True
                    q.append(v)
        return False 