# Last updated: 29/12/2025, 03:02:41
class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        indices = []
        res = []
        for i, num in enumerate(nums):
            if num == x:
                indices.append(i)
        
        for q in queries:
            if q > len(indices):
                res.append(-1)
            else:
                res.append(indices[q-1])
        return res
        