"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        for i in sorted_intervals:
            print(i.start)
        end = -1
        for interval in sorted_intervals:
            if interval.start < end:
                return False
            end = max(end, interval.end)
        return True