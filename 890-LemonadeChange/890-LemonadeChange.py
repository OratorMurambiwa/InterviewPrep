# Last updated: 31/12/2025, 18:43:44
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0

        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                five, ten = five - 1, ten + 1
            else:
                if ten > 0:
                    five, ten = five - 1, ten-1
                else:
                    five -=3
            if five < 0:
                return False
            
        return True
        