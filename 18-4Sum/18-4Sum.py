# Last updated: 19/01/2026, 10:56:07
1class Solution(object):
2    def fourSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[List[int]]
7        """
8        nums.sort()
9        res = []
10        n = len(nums)
11
12        for i in range(n-3):
13            if i > 0 and nums[i] == nums[i-1]:
14                continue
15
16            for j in range(i+1, n-2):
17                if j > i+1 and nums[j] == nums[j-1]:
18                    continue
19
20                l, r = j+1, n-1
21                while l < r:
22                    sum = nums[i] + nums[j] + nums[l] + nums[r]
23
24                    if sum == target:
25                        res.append([nums[i], nums[j], nums[l], nums[r]])
26                        l +=1
27                        r-=1
28
29                        while l < r and nums[l] == nums[l-1]:
30                            l+=1
31                        while l < r and nums[r] == nums[r+1]:
32                            r-=1
33                    
34                    elif sum < target:
35                        l+=1
36                    else:
37                        r -=1
38        return res
39            