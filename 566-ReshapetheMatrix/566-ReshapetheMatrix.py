# Last updated: 05/01/2026, 23:04:25
1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        seen = {}
9
10        for i, num in enumerate(nums):
11            complement = target - num
12            if complement in seen:
13                return [seen[complement], i]
14            seen[num] = i
15