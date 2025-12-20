class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        stack = [source]
        visited[source] = True

        while stack:
            node = stack.pop()
            if node == destination:
                return True 
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    stack.append(neighbour)
        return False

