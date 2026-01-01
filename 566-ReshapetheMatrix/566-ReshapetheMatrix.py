# Last updated: 31/12/2025, 22:33:51
1class Solution(object):
2    def lengthOfLongestSubstring(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        if len(s) == 0:
8            return 0
9
10        char_set = set()
11        maxlen = 0
12        left = 0
13
14        for i in range(len(s)):
15            while s[i] in char_set:
16                char_set.remove(s[left])
17                left += 1
18
19            char_set.add(s[i])
20            maxlen = max(maxlen, i - left + 1)
21
22        return maxlen