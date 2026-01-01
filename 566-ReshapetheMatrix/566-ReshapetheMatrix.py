# Last updated: 31/12/2025, 21:30:33
1class Solution(object):
2    def longestPalindrome(self, words):
3        """
4        :type words: List[str]
5        :rtype: int
6        """
7        count = Counter(words)
8        length = 0
9        center = False
10
11        for word, freq in count.items():
12            rev = word[::-1]
13
14            if word == rev:
15                length += (freq//2) * 4
16                if freq % 2 == 1:
17                    center = True
18
19            elif word < rev:
20                pairs = min(freq, count[rev])
21                length += pairs * 4
22
23        if center:
24            length +=2
25
26        return length