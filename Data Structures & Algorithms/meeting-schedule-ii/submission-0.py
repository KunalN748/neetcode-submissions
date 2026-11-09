"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        priority_queue = []
        for interval in sorted_intervals:
            if not priority_queue:
                heapq.heappush(priority_queue, interval.end)
                continue
            if priority_queue[0] <= interval.start:
                heapq.heappop(priority_queue)
                heapq.heappush(priority_queue, interval.end)
            else:
                heapq.heappush(priority_queue, interval.end)
        return len(priority_queue)
        