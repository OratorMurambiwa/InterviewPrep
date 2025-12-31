# Last updated: 30/12/2025, 20:33:04
1class Solution(object):
2    def minEatingSpeed(self, piles, h):
3        """
4        :type piles: List[int]
5        :type h: int
6        :rtype: int
7        """
8        l, r = 1, max(piles)
9        res = r
10
11        while l <= r:
12            k = (l+r)//2
13
14            total = 0
15            for p in piles:
16                total += (p//k)
17                if p % k != 0:
18                    total += 1
19            
20            if total <= h:
21                res = k
22                r = k - 1
23            else:
24                l = k + 1
25        return res
26
27
28                
29            
30
31        