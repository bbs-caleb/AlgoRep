class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)
        
        visited = [False] * n 
        q = deque([source])
        visited[source] = True

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
        return False