# Last updated: 19/01/2026, 12:45:33
1class Solution(object):
2    def largestOverlap(self, img1, img2):
3        """
4        :type img1: List[List[int]]
5        :type img2: List[List[int]]
6        :rtype: int
7        """
8        n = len(img1)
9        one1 = []
10        one2 = []
11        shift = Counter()
12
13        for i in range(n):
14            for j in range(n):
15                if img1[i][j] == 1:
16                    one1.append((i, j))
17                if img2[i][j] == 1:
18                    one2.append((i,j))
19
20        for x1, y1 in one1:
21            for x2, y2 in one2:
22                dx = x2 - x1
23                dy = y2 - y1
24                shift[(dx,dy)] += 1
25
26        return max(shift.values() or [0])
27
28        