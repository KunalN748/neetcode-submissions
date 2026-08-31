class Solution:
    def hammingWeight(self, n: int) -> int:
        d = Counter(bin(n))
        return d["1"]