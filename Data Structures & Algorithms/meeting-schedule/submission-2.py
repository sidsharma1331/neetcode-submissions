"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        for i in range(n):
            start = intervals[i].start
            end = intervals[i].end
            for j in range(n):
                s, e = intervals[j].start, intervals[j].end
                if i!=j:
                    if (s<start and e>start) or (s<end and e>end) or (s==start and e==end):
                        print(s,e, start, end)
                        return False
        return True

