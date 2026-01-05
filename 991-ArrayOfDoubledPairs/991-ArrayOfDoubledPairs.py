# Last updated: 04/01/2026, 21:14:49
class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        count = Counter(arr)

        for x in sorted(arr, key = abs):
            if count[x] == 0:
                continue
            if count[2*x] == 0:
                return False
            count[x] -=1
            count[2*x] -=1
        return True
        
        