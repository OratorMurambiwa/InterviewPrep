# Last updated: 31/12/2025, 18:43:43
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2

            total = 0
            for p in piles:
                total += (p//k)
                if p % k != 0:
                    total += 1
            
            if total <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res


                
            

        