class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = dict(Counter(s1))
        compare = d
        l, r = 0, 0 
        while r < len(s2):
            if s2[r] not in d:
                if l != r:
                    d[s2[l]] = d.get(s2[l], 0) + 1
                    l += 1
                else:
                    l += 1
                    r += 1

            else:
                print(s2[r])
                if d[s2[r]] == 1:
                    del d[s2[r]]
                else:
                    d[s2[r]] -= 1
                if (r-l+1) == len(s1) and not d:
                    return True
                r += 1
        return False