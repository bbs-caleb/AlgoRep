class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)), 0, -1):
            word = str1[:i]
            if (len(str1) % i == 0 and len(str2) % i == 0
                and word * (len(str1) // i) == str1 and word * (len(str2) // i) == str2):
                return word
        return ""