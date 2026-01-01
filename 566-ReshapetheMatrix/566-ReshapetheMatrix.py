# Last updated: 31/12/2025, 20:45:11
1class Solution(object):
2    def longestPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        freq = defaultdict(int)
8
9        for char in s:
10            freq[char] += 1
11        
12        length = 0
13        odd = False
14
15        for count in freq.values():
16            if count % 2 == 0:
17                length += count
18            else:
19                length += count -1
20                odd = True
21        
22        if odd:
23            return length + 1
24        else:
25            return length
26
27
28        