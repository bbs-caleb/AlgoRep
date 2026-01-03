class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1

        lst = list(s)
        while i < j:
            if lst[i].isalpha() and lst[j].isalpha():
                lst[i], lst[j] = lst[j], lst[i]
                i, j = i + 1, j - 1
            else:
                if not lst[i].isalpha():
                    i += 1 
                if not lst[j].isalpha():
                    j -= 1
        return "".join(lst)