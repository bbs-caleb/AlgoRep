1from typing import List
2import heapq
3
4class Solution:
5    def maxSum(self, nums: List[int], threshold: List[int]) -> int:
6        n = len(nums)
7        items = sorted(zip(threshold, nums)) 
8        
9        max_heap = []  
10        total = 0
11        step = 1
12        ptr = 0  
13        
14        while True:
15            while ptr < n and items[ptr][0] <= step:
16                t, val = items[ptr]
17                heapq.heappush(max_heap, -val)  
18                ptr += 1
19            
20            if not max_heap:
21                break
22            
23            best_val = -heapq.heappop(max_heap)
24            total += best_val
25            
26            step += 1  
27        return total
28