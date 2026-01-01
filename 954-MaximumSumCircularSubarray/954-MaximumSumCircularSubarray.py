# Last updated: 31/12/2025, 18:43:42
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cmax = 0
        cmin = 0
        gmax = nums[0]
        gmin = nums[0]
        total = 0

        for num in nums:
            cmax = max(cmax + num, num)
            cmin = min(cmin+num, num)
            total += num 
            gmax = max(gmax, cmax)
            gmin = min(gmin, cmin)
        
        if gmax > 0:
            return max(gmax, total-gmin)
        else:
            return gmax
        