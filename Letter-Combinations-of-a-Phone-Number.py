1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        if not digits:
4            return []
5
6        phone = {
7            "2": "abc",
8            "3": "def",
9            "4": "ghi",
10            "5": "jkl",
11            "6": "mno",
12            "7": "pqrs",
13            "8": "tuv",
14            "9": "wxyz",
15        }
16
17        res = []
18        path = []
19
20        def dfs(idx: int) -> None:
21            if idx == len(digits):
22                res.append("".join(path))
23                return
24
25            letters = phone[digits[idx]]
26            for ch in letters:
27                path.append(ch)
28                dfs(idx + 1)
29                path.pop()
30
31        dfs(0)
32        return res
33