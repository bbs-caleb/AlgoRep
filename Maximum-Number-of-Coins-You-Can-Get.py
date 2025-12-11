1class Solution:
2    def maxCoins(self, piles: List[int]) -> int:
3        piles.sort()
4        
5        n = len(piles) // 3
6        return sum(piles[n::2])
7        