1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        rows, cols = len(board), len(board[0])
4        
5        def backtrack(r, c, k):
6            if k == len(word):
7                return True
8            
9            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]):
10                return False
11
12            temp = board[r][c]
13            board[r][c] = '#'
14            
15            found = (backtrack(r + 1, c, k + 1) or backtrack(r - 1, c, k + 1) or backtrack(r, c + 1, k + 1) or backtrack(r, c - 1, k + 1))
16            board[r][c] = temp
17            
18            return found
19
20        for r in range(rows):
21            for c in range(cols):
22                if board[r][c] == word[0] and backtrack(r, c, 0):
23                    return True
24                    
25        return False