1class Solution:
2    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
3        if source == destination:
4            return True
5        
6        graph = [[] for _ in range(n)]
7
8        for u, v in edges:
9            graph[u].append(v)
10            graph[v].append(u)
11        
12        visited = [False] * n 
13        stack = [source]
14        visited[source] = True
15
16        while stack:
17            node = stack.pop()
18            if node == destination:
19                return True
20            for neigh in graph[node]:
21                if not visited[neigh]:
22                    visited[neigh] = True
23                    stack.append(neigh)
24        return False