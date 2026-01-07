# Last updated: 07/01/2026, 14:10:25
1class Solution(object):
2    def eraseOverlapIntervals(self, intervals):
3        """
4        :type intervals: List[List[int]]
5        :rtype: int
6        """
7        intervals.sort()
8        count = 0
9        lastend = intervals[0][1]
10
11        for start, end in intervals[1:]:
12            if start >= lastend:
13                lastend = end
14            else:
15                count +=1
16                lastend = min(end, lastend)
17        return count