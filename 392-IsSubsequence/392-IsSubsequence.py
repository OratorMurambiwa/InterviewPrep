# Last updated: 29/12/2025, 03:03:03
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0

        for j in t:
            if i < len(s) and s[i] == j:
                i += 1

        return i == len(s)
        