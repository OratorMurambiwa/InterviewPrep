# Last updated: 29/12/2025, 03:03:59
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current_max = res = nums[0]

        for i in nums[1:]:
            current_max = max(i, current_max + i)
            res = max(res, current_max)
        return res
        