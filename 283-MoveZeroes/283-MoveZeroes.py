# Last updated: 29/12/2025, 03:03:12
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastposition = 0

        for num in range(len(nums)):
            if nums[num] != 0:
                nums[lastposition], nums[num] = nums[num], nums[lastposition]
                lastposition += 1
        