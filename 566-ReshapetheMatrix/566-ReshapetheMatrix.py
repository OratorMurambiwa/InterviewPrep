# Last updated: 05/01/2026, 23:18:06
1class Solution(object):
2    def threeSum(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7        nums.sort()
8        res = []
9
10        for i in range(len(nums)):
11            if i > 0 and nums[i] == nums[i-1]:
12                continue
13
14            l, r = i + 1, len(nums) - 1
15
16            while l < r:
17                total = nums[i] + nums[l] + nums[r]
18                if total < 0:
19                    l +=1
20                elif total > 0:
21                    r -= 1
22                else:
23                    res.append([nums[i], nums[l], nums[r]])
24
25                    l +=1
26                    r -= 1
27                    while l < r and nums[l] == nums[l-1]:
28                        l += 1
29                    while l < r and nums[r] == nums[r+1]:
30                        r -= 1
31
32        return res
33        