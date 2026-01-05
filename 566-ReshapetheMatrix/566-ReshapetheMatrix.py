# Last updated: 04/01/2026, 21:14:17
1class Solution(object):
2    def findPairs(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        # if k < 0:
9        #     return 0
10
11        freq = defaultdict(int)
12
13        for x in nums:
14            freq[x] += 1
15
16        count = 0
17        
18        if k == 0:
19            for x in freq:
20                if freq[x] > 1:
21                    count += 1
22            return count
23
24        for x in freq:
25            if x + k in freq:
26                count += 1
27        return count
28
29
30
31
32