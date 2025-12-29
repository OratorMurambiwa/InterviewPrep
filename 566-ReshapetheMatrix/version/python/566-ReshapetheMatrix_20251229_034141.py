# Last updated: 29/12/2025, 03:41:41
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        totalCash = 0 
        changeNeeded = 0

        changeBills = []

        for num in bills:
            if num == 5:
                changeBills.append(num)
            elif num == 10 and changeBills.count(5) >= 1:
                changeBills.remove(5)
                changeBills.append(10)
            elif num == 10 and changeBills.count(5) < 1:
                print('no change for a 10')
                return False 
            elif num == 20 and changeBills.count(5) >= 1 and changeBills.count(10) >= 1:
                changeBills.remove(5)
                changeBills.remove(10)
            elif num == 20 and changeBills.count(5) >= 3:
                changeBills.remove(5)
                changeBills.remove(5)
                changeBills.remove(5)
            elif num == 20 and ((changeBills.count(5) < 3) or (changeBills.count(5) < 1 and changeBills.count(10) < 1)):
                print('no change for a 20')
                return False
        
        return True
            






        