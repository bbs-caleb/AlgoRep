1class Solution:
2    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
3        if source == destination:
4            return True
5        
6        graph = [[] for _ in range(n)]
7        for u, v in edges:
8            graph[u].append(v)
9            graph[v].append(u)
10        
11        visited = [False] * n
12        stack = [source]
13        visited[source] = True
14
15        while stack:
16            node = stack.pop()
17            if node == destination:
18                return True 
19            for neighbour in graph[node]:
20                if not visited[neighbour]:
21                    visited[neighbour] = True
22                    stack.append(neighbour)
23        return False
24
25