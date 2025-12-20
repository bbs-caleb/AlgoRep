1class Solution:
2    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
3        if source == destination:
4            return True
5        
6        graph = [[] for _ in range(n)]
7        for u, v in edges:
8            graph[v].append(u)
9            graph[u].append(v)
10        
11        visited = [False] * n 
12        q = deque([source])
13        visited[source] = True
14
15        while q:
16            node = q.popleft()
17            if node == destination:
18                return True
19            for neighbor in graph[node]:
20                if not visited[neighbor]:
21                    visited[neighbor] = True
22                    q.append(neighbor)
23        return False