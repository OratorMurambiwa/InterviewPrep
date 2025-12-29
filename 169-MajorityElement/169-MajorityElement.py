# Last updated: 29/12/2025, 03:03:32
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequent = None
        count = 0

        for num in nums:
            if count == 0:
                frequent = num
            if frequent == num:
                count += 1
            else:
                count -= 1

        return frequent