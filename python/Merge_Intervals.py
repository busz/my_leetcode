'''
Created on 2014.8.10

Leetcode : Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].


'''
# Definition for an interval.

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key = lambda item : item.start);
        pos = 0
        
        while pos < len(intervals) - 1:
            if intervals[pos].end >= intervals[pos+1].start:
                if intervals[pos].end < intervals[pos+1].end:
                    intervals[pos].end = intervals[pos+1].end
                del intervals[pos+1]
            else:
                pos = pos + 1
        return intervals
    
test = Solution()
intervals = []
intervals.append(Interval(1,3))
intervals.append(Interval(2,6))
intervals.append(Interval(8,10))
intervals.append(Interval(15,18))

r =  test.merge(intervals)
for item in intervals:
    print item.start , item.end
