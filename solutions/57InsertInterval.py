# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]. 
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        if not intervals or len(intervals) == 0:
            res.append(newInterval)
            newInterval = None
        for i in intervals:
            if not newInterval:
                if res[-1].end < i.start:
                    res.append(i)
                elif res[-1].end < i.end:
                    res[-1].end = i.end
            else:
                if i.end < newInterval.start:
                    res.append(i)
                elif i.end <= newInterval.end:
                    if i.start < newInterval.start:
                        tmp = Interval(i.start, newInterval.end)
                        res.append(tmp)
                    else:
                        res.append(newInterval)
                    newInterval = None
                elif i.end > newInterval.end:
                    if i.start < newInterval.start:
                        res.append(i)
                    elif i.start <= newInterval.end:
                        tmp = Interval(newInterval.start, i.end)
                        res.append(tmp)
                    else:
                        res.append(newInterval)
                        res.append(i)
                    newInterval = None
        if newInterval:
            res.append(newInterval)
        return res
                        

# much much much more concise!
def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left = [i for i in intervals if i.end < s]
    right = [i for i in intervals if i.start > e]
    if left + right != intervals:
        s = min(s, intervals[len(left)].start)
        e = max(e, intervals[~len(right)].end)
    return left + [Interval(s, e)] + right
