class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-z0-9]", "", s)
        r = len(s) - 1
        for l in range(len(s)//2):
            if s[l] != s[r]:
                return False
            r -= 1
        return True