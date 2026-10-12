class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 == 1:
           return False

        target = total // 2
        
        seen = set()
        seen.add(0)

        for num in nums:
            new_seen = set()
            for works in seen:
                if (works+num) == target:
                    return True
                elif (works+num) < target:
                    new_seen.add(works+num)
            seen.update(new_seen)
        return False