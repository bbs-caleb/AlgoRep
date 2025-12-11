class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        buckets = defaultdict(list) 
        res: List[List[int]] = []

        for i, size in enumerate(groupSizes):
            buckets[size].append(i)
            if len(buckets[size]) == size:
                res.append(buckets[size])
                buckets[size] = []  
        return res
