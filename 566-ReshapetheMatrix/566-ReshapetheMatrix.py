# Last updated: 07/01/2026, 13:37:58
1class Solution(object):
2    def insert(self, intervals, newInterval):
3        """
4        :type intervals: List[List[int]]
5        :type newInterval: List[int]
6        :rtype: List[List[int]]
7        """
8        
9        res = []
10
11        for i in range(len(intervals)):
12            if newInterval[1] < intervals[i][0]:
13                res.append(newInterval)
14                return res + intervals[i:]
15            elif newInterval[0] > intervals[i][1]:
16                res.append(intervals[i])
17            else:
18                newInterval = [
19                    min(newInterval[0], intervals[i][0]),
20                    max(newInterval[1], intervals[i][1])
21                ]
22        res.append(newInterval)
23
24        return res