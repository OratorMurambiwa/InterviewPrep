# Last updated: 05/01/2026, 13:51:29
1class Solution(object):
2    def numberOfSubarrays(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        res = 0
9        l = 0
10        m = 0
11        odd = 0
12
13        for r in range(len(nums)):
14            if nums[r] % 2:
15                odd += 1
16                m = l  
17
18            while odd > k:
19                if nums[l] % 2:
20                    odd -= 1
21                l += 1
22                m = l  
23
24            if odd == k:
25                while m <= r and nums[m] % 2 == 0:
26                    m += 1
27                res += (m - l + 1)
28
29        return res
30
31
32
33