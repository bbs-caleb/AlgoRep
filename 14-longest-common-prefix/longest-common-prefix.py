class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            for word in strs[1:]:
                if len(word) == i or first[i] != word[i]:
                    return first[:i]
        return first             
            