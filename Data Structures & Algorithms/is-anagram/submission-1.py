class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for char in s:
            d[char] = d.get(char, 0) + 1
        for char in t:
            if char not in d or d[char] == 0:
                return False
            d[char] = d.get(char) - 1
        return True