# Last updated: 29/12/2025, 03:03:14
class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #find length of array
        n = len(nums)
        #create new array for answers
        answers = [1] * n
        #set prefix to 1
        prefix = 1
        #iterate through n and multiply each i i n answers with i in nums from left
        for i in range(n):
            answers[i] = prefix
            prefix *= nums[i]
        #set suffix to 1
        postfix = 1
        #iterate through n from right 
        for i in range(n-1, -1, -1):
            answers[i] *= postfix
            postfix *= nums[i]
        #suffix multiplied by answer i to get new suffix, then by nums i and save in ans

        return answers      