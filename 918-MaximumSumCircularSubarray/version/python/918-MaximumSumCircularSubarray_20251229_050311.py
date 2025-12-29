# Last updated: 29/12/2025, 05:03:11
1class Solution(object):
2    def maxSubarraySumCircular(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        cmax = 0
8        cmin = 0
9        gmax = nums[0]
10        gmin = nums[0]
11        total = 0
12
13        for num in nums:
14            cmax = max(cmax + num, num)
15            cmin = min(cmin+num, num)
16            total += num 
17            gmax = max(gmax, cmax)
18            gmin = min(gmin, cmin)
19        
20        if gmax > 0:
21            return max(gmax, total-gmin)
22        else:
23            return gmax
24        