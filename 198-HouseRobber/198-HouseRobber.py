# Last updated: 01/01/2026, 19:50:36
1class Solution(object):
2    def rob(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        prevh = 0
8        prev2h = 0
9
10        for i in nums:
11            new_total = max(prevh, prev2h + i)
12            prev2h = prevh
13            prevh = new_total
14
15        return prevh
16        