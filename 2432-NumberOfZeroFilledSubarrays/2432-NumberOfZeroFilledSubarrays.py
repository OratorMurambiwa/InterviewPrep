# Last updated: 29/12/2025, 03:02:42
class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        streak = 0

        for i in nums:
            if i == 0:
                streak += 1
                counter += streak
            else:
                streak = 0

        return counter
        