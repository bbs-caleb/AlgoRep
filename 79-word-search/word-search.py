class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def backtrack(r, c, k):
            if k == len(word):
                return True
            
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]):
                return False

            temp = board[r][c]
            board[r][c] = '#'
            
            found = (backtrack(r + 1, c, k + 1) or backtrack(r - 1, c, k + 1) or backtrack(r, c + 1, k + 1) or backtrack(r, c - 1, k + 1))
            board[r][c] = temp
            
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True
                    
        return False