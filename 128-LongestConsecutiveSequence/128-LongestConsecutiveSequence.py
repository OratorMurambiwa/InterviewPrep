# Last updated: 29/12/2025, 03:03:41
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        maxlength = 0

        for num in numset:
            if num -1 not in numset:
                length = 1
                curr = num

                while curr + 1 in numset:
                    curr += 1
                    length += 1

                maxlength = max(maxlength, length)
        return maxlength
    
        