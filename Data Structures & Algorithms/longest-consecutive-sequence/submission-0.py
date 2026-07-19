class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        length = 0
        for i in nums:
            if i-1 not in nums:
                loc = 1
                while i+1 in nums:
                    loc += 1
                    i = i+1
                length = max(length, loc)
        return length