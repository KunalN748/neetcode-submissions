class Solution:
    def hammingWeight(self, n: int) -> int:
        d = Counter(bin(n))
        print(d)
        return d["1"]