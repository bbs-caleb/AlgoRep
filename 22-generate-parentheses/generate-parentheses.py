class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(open_cnt, close_cnt, stack):
            if open_cnt == n and close_cnt == n:
                result.append("".join(stack))
                return

            if open_cnt < n:
                stack.append("(")                  
                backtrack(open_cnt + 1, close_cnt, stack) 
                stack.pop()                         

            if close_cnt < open_cnt:
                stack.append(")")                   
                backtrack(open_cnt, close_cnt + 1, stack) 
                stack.pop()                        

        backtrack(0, 0, [])
        return result