class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        dp = [0] * (n + 1)
        best = 0

        for i in range(m, n + 1):
            if sequence[i - m:i] == word:
                dp[i] = dp[i - m] + 1
                if best < dp[i]:
                    best = dp[i]
        return best 