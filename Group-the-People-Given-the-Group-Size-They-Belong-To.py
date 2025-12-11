1class Solution:
2    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
3        buckets = defaultdict(list) 
4        res: List[List[int]] = []
5
6        for i, size in enumerate(groupSizes):
7            buckets[size].append(i)
8            if len(buckets[size]) == size:
9                res.append(buckets[size])
10                buckets[size] = []  
11        return res
12