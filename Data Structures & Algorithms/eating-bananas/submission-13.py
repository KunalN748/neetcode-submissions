class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallest = max(piles)
        l = 1
        r = max(piles)
        while l <= r: 
            mid = (l + r) // 2
            print("mid: " + str(mid))
            time = 0
            for i in piles:
                if i % mid != 0:
                    time += 1
                time += (i // mid) 
            print(time)
            if time <= h:
                r = mid - 1
                smallest = min(smallest, mid)
            else:
                l = mid + 1
        return smallest

