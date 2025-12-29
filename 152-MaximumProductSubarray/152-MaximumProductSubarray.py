# Last updated: 29/12/2025, 03:03:30
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        understand
            input - array of integers nums
            output - integer(largest product of a subarray)
            constraint - it is a subarray
            edge cases - array with one integer
        hlp - set current max, current min and res to nums[0]
            - loop through nums from second integer
            - if the integer is less than zero, flip current max and current min
            - current max will be max of that integer and current max * integer
            - current min will be min of that integer and current min * integer
            - final result will be max of current max and res
            - return res
        """
        current_max = current_min = res = nums[0]

        for i in nums[1:]:
            if i < 0:
                current_max, current_min = current_min, current_max

            current_max = max(i, current_max * i)
            current_min = min(i, current_min * i)

            res = max(res, current_max)
        return res