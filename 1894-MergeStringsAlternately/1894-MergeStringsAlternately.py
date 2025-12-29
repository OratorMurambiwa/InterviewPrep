# Last updated: 29/12/2025, 03:02:45
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n1=len(word1)
        n2=len(word2)
        n=min(n1, n2)
        result=""

        for i in range(n):
            result += word1[i] + word2[i]
        if n1 == n2:
            return result
        elif n1 >= n2:
            return result + word1[n:]
        else:
            return result + word2[n:] 