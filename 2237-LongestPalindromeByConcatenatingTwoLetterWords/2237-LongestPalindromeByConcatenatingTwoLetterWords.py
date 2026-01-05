# Last updated: 04/01/2026, 21:14:40
class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = Counter(words)
        length = 0
        center = False

        for word, freq in count.items():
            rev = word[::-1]

            if word == rev:
                length += (freq//2) * 4
                if freq % 2 == 1:
                    center = True

            elif word < rev:
                pairs = min(freq, count[rev])
                length += pairs * 4

        if center:
            length +=2

        return length