# Last updated: 29/12/2025, 04:11:44
1class Solution(object):
2    def maxSubArray(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        maxSum = nums[0]
8        currSum = 0
9
10        for i in range(len(nums)):
11            if currSum < 0:
12                currSum = 0
13            currSum += nums[i]
14            maxSum = max(maxSum, currSum)
15        return maxSum