# Last updated: 29/12/2025, 03:02:46
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxcandies = max(candies) 

        return[(candy + extraCandies >= maxcandies) for candy in candies]  