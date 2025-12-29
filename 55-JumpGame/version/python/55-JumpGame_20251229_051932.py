# Last updated: 29/12/2025, 05:19:32
1class Solution(object):
2    def canJump(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        target = len(nums) -1
8
9
10        for i in range(len(nums) -2, -1, -1):
11            if i + nums[i] >= target:
12                target = i
13        return target == 0
14            
15
16        