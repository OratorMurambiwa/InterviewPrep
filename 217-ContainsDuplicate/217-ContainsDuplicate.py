# Last updated: 29/12/2025, 03:03:17
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # seen = []
        # counter = 0

        # for i in nums:
        #     if i in seen:
        #         counter += 1
        #     else:
        #         seen.append(i)

        # return counter != 0

        return len(nums) != len(set(nums))