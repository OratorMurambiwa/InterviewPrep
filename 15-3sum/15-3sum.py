# Last updated: 29/12/2025, 03:04:11
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        understand
                i - array of integers nums
                o - list of all the triplets of integers = 0
                c - no duplicate triplets
                e - if none of the integers add up to zero, return empty list

        HLP - create an empty list to store results
            - sort the array
            -iterate through nums looking at both the index and the values
            - check if (a) is the first ie i > 0 and a == [i-1], if it is, conitnue becaue
             we have already seen it before
            -initialise two pointers, left = i+1 and right = len(nums) - 1
            - while left < right:
            - 3sum = a + nums[left] + nums[right]
            - if 3sum > 0, right -=1
            -elif 3sum < 0, left += 1
            -else 3sum is equal to 0, append all three to the list storing results
            - shift left to the right
            - while nums[left] = nums[left - 1] and left < right, left += 1
            - return list of results
        """

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tsum = a + nums[left] + nums[right]
                if tsum > 0:
                    right -= 1
                elif tsum < 0:
                    left +=1
                else:
                    res.append([a, nums[left], nums[right]])
                    left +=1
                    while nums[left] == nums[left - 1] and left < right:
                        left +=1
        return res
        