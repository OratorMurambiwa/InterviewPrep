# Last updated: 29/12/2025, 03:37:27
# time = O(n), Space = O(1)
1class Solution(object):
2    def lemonadeChange(self, bills):
3        """
4        :type bills: List[int]
5        :rtype: bool
6        """
7        five = ten = 0
8
9        for b in bills:
10            if b == 5:
11                five += 1
12            elif b == 10:
13                five, ten = five - 1, ten + 1
14            else:
15                if ten > 0:
16                    five, ten = five - 1, ten-1
17                else:
18                    five -=3
19            if five < 0:
20                return False
21            
22        return True
23        