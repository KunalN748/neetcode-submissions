class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
            
        max_len = 0
        l, r = 0, 1
        placeholder = s[l]

        while r < len(s):
            if s[r] in placeholder:
                max_len = max(max_len, len(placeholder))
                while(s[r] in placeholder):
                    l += 1
                    placeholder = placeholder[1:]
            placeholder += s[r]
            r+=1
        max_len = max(max_len, len(placeholder))
        return max_len