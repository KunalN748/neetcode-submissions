class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        result = r
        while l <= r:
            mid = (l+r)//2
            time = 0
            for i in range(len(piles)):
                time += piles[i] // mid
                if piles[i] % mid != 0:
                    time += 1
            if time <= h:
                result = min(result, mid)
                r = mid - 1
            elif time > h:
                l = mid + 1
        return result
