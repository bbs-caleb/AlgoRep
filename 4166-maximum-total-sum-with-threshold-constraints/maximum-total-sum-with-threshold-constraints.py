from typing import List
import heapq

class Solution:
    def maxSum(self, nums: List[int], threshold: List[int]) -> int:
        n = len(nums)
        items = sorted(zip(threshold, nums)) 
        
        max_heap = []  
        total = 0
        step = 1
        ptr = 0  
        
        while True:
            while ptr < n and items[ptr][0] <= step:
                t, val = items[ptr]
                heapq.heappush(max_heap, -val)  
                ptr += 1
            
            if not max_heap:
                break
            
            best_val = -heapq.heappop(max_heap)
            total += best_val
            
            step += 1  
        return total
