# Last updated: 29/12/2025, 03:03:19
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def rob_c(nums):
            prev = curr = 0

            for num in nums:
                prev, curr = curr, max(prev + num, curr)

            return curr

        
        return max(rob_c(nums[1:]), rob_c(nums[:-1]))




    
        