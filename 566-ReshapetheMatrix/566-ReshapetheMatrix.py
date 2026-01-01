# Last updated: 31/12/2025, 20:17:18
1class Solution(object):
2    def canReorderDoubled(self, arr):
3        """
4        :type arr: List[int]
5        :rtype: bool
6        """
7
8        count = Counter(arr)
9
10        for x in sorted(arr, key = abs):
11            if count[x] == 0:
12                continue
13            if count[2*x] == 0:
14                return False
15            count[x] -=1
16            count[2*x] -=1
17        return True
18        
19        