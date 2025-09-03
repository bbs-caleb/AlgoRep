class Solution:
    def numberCount(self, a: int, b: int) -> int:
        def count_up_to(n: int) -> int:
            if n <= 0:
                return 0
            s = str(n)

            @lru_cache(maxsize=None)
            def dp(pos: int, mask: int, tight: bool, started: bool) -> int:
                if pos == len(s):
                    return 1 if started else 0

                res = 0
                lim = int(s[pos]) if tight else 9

                if not started:
                    next_tight = tight and (0 == lim)
                    res += dp(pos + 1, mask, next_tight, False)

                start_d = 1 if not started else 0
                for d in range(start_d, lim + 1):
                    if (mask >> d) & 1:
                        continue
                    next_tight = tight and (d == lim)
                    res += dp(pos + 1, mask | (1 << d), next_tight, True)

                return res

            return dp(0, 0, True, False)

        return count_up_to(b) - count_up_to(a - 1)