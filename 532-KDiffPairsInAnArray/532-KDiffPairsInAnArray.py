# Last updated: 04/01/2026, 21:14:56
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # if k < 0:
        #     return 0

        freq = defaultdict(int)

        for x in nums:
            freq[x] += 1

        count = 0
        
        if k == 0:
            for x in freq:
                if freq[x] > 1:
                    count += 1
            return count

        for x in freq:
            if x + k in freq:
                count += 1
        return count




