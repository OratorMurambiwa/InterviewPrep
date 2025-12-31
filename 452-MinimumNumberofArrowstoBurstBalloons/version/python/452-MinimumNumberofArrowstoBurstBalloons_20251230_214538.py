# Last updated: 30/12/2025, 21:45:38
1class Solution(object):
2    def findMinArrowShots(self, points):
3        """
4        :type points: List[List[int]]
5        :rtype: int
6        """
7        points.sort()
8
9        minarrows = len(points)
10        prev = points[0]
11
12        for p in range(1, len(points)):
13            curr = points[p]
14            if curr[0] <= prev[1]:
15                minarrows -= 1
16                prev = [curr[0], min(curr[1], prev[1])]
17            else:
18                prev = curr
19
20        return minarrows