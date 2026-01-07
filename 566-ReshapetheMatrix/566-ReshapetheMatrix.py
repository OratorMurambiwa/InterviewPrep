# Last updated: 07/01/2026, 13:56:25
1class Solution(object):
2    def merge(self, intervals):
3        """
4        :type intervals: List[List[int]]
5        :rtype: List[List[int]]
6        """
7        intervals.sort()
8
9        res = [intervals[0]]
10
11        for start, end in intervals[1:]:
12            lastend = res[-1][1]
13            if start <= lastend:
14                res[-1][1] = max(lastend, end)
15            else:
16                res.append([start, end])
17
18        return res
19