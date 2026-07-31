class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        buckets = [[] for i in range(len(nums)+1)]
         
        for n, f in freq.items():
            buckets[f].append(n)
        
        res = []
        for i in range(len(buckets)-1,-1,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k: 
                    return res