# Last updated: 29/12/2025, 03:03:07
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float("inf")
        second = float("inf")

        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True

        return False


