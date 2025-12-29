# Last updated: 29/12/2025, 03:02:51
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        remainders = [0] * 60
        pairs = 0

        for i in time:
            r = i % 60
            complement = (60 -r) % 60
            pairs += remainders[complement]
            remainders[r] += 1

        return pairs
 
        