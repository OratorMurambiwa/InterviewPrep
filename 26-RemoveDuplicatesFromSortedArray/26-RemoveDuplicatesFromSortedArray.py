# Last updated: 29/12/2025, 03:04:06
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       #check if nums is empty, if so return 0
        if not nums:
            return 0

       #initialise a pointer and set it to 0
        j = 0

       #iterate through nums, if index at a num is not equal to pointer
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
            nums[j] = nums[i]

       # if so unique value and increment the pointer by 1
       # add the unique element to correct position
       #return j + 1

        return j + 1


        