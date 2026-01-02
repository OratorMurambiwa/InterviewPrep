# Last updated: 02/01/2026, 07:32:07
1class Solution(object):
2    def singleNumber(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        numset = Counter(nums)
8
9        for i in nums:
10            if numset[i] == 1:
11                return i 
12        