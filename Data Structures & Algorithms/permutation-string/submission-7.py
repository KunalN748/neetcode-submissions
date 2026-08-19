class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0 
        target = Counter(s1)
        window = Counter(s2[:len(s1)])

        if target == window:
                return True

        for r in range(len(s1), len(s2)):
            window[s2[r]] += 1
            left_char = s2[r - len(s1)]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if target == window:
                return True

        return False
            