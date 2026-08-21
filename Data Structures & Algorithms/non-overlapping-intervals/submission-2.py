class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i, n = 0, len(intervals)
        total = 0
        deleted = []
        while i < n:
            j = i + 1
            while j < n and intervals[j][0] < intervals[i][1]:
                if intervals[j][1] < intervals[i][1]:
                    i = j
                total += 1    
                j += 1  
            i = j
        return total