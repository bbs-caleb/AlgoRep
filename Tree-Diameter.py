1import collections
2
3class Solution:
4    def treeDiameter(self, edges: List[List[int]]) -> int:
5        graph = collections.defaultdict(list)
6        for u, v in edges:
7            graph[u].append(v)
8            graph[v].append(u)
9            
10        self.diameter = 0
11        
12        def dfs(node, parent):
13            max_depth_1 = 0 
14            max_depth_2 = 0 
15            
16            for neighbor in graph[node]:
17                if neighbor == parent:
18                    continue
19                
20                depth = dfs(neighbor, node)
21                
22                if depth > max_depth_1:
23                    max_depth_2 = max_depth_1
24                    max_depth_1 = depth
25                elif depth > max_depth_2:
26                    max_depth_2 = depth
27            
28            self.diameter = max(self.diameter, max_depth_1 + max_depth_2)
29            
30            return max_depth_1 + 1
31            
32        dfs(0, -1)
33        return self.diameter