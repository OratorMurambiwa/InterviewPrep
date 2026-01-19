# Last updated: 19/01/2026, 11:14:56
1class Solution(object):
2    def fourSumCount(self, nums1, nums2, nums3, nums4):
3        """
4        :type nums1: List[int]
5        :type nums2: List[int]
6        :type nums3: List[int]
7        :type nums4: List[int]
8        :rtype: int
9        """
10        sumAB = defaultdict(int)
11        res = 0
12
13        for a in nums1:
14            for b in nums2:
15                total = a + b
16                sumAB[total] +=1
17        
18        for c in nums3:
19            for d in nums4:
20                cd_total = c + d
21                needed = -cd_total
22                res += sumAB[needed]
23        
24        return res