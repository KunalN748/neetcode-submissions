class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for n, f in freq.items():
            buckets[f].append(n)
        
        result = []
        for i in range(len(buckets)-1,-1,-1):
            for j in buckets[i]:
                result.append(j)
                if len(result) == k:
                    return result




