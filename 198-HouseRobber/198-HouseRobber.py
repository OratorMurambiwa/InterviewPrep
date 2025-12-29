# Last updated: 29/12/2025, 03:03:25
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums)==1:
            return nums[0]

        prev = curr = 0

        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        
        return curr
        



        