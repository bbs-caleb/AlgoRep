class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        path = []

        def dfs(idx: int) -> None:
            if idx == len(digits):
                res.append("".join(path))
                return

            letters = phone[digits[idx]]
            for ch in letters:
                path.append(ch)
                dfs(idx + 1)
                path.pop()

        dfs(0)
        return res
