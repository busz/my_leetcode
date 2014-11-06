'''
Created on 2014.8.14

leetcode Insert_Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals 

(merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

'''

# Definition for an interval.

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        pos = 0
        if newInterval.end < intervals[0].start:
            intervals = [newInterval] + intervals
            return intervals
        elif  newInterval.start <= intervals[0].end:
            intervals[0].start = min(intervals[0].start , newInterval.start)
            intervals[0].end = max(intervals[0].end , newInterval.end)
        else:
            while pos < len(intervals):
                if newInterval.start > intervals[pos].end:
                    pos += 1
                elif newInterval.start == intervals[pos].end:
                    intervals[pos].end = newInterval.end
                    break
                elif newInterval.start <= intervals[pos].end and newInterval.end >= intervals[pos].start:
                    intervals[pos].start = min(intervals[pos].start , newInterval.start)
                    intervals[pos].end = max(intervals[pos].end , newInterval.end)
                    break
                else:
                    intervals = intervals[:pos]+[newInterval] + intervals[pos:]
                    return intervals
            if pos == len(intervals) :
                intervals.append(newInterval)
        while pos < len(intervals) - 1:
            if intervals[pos].end < intervals[pos+1].start:
                break
            elif intervals[pos].end >= intervals[pos+1].end:
                del intervals[pos+1]
            else:
                intervals[pos].end = intervals[pos+1].end
                del intervals[pos+1]
        return intervals
                
        
       
