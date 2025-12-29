# Last updated: 29/12/2025, 03:02:49
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n1=len(str1)
        n2=len(str2)
        n=min(n1, n2)

        def isDivisor(l):
            if n1%l or n2%l:
                return False
            f1=n1//l
            f2=n2//l
            return str1[:l]*f1 == str1 and str1[:l]*f2 == str2

        for l in range(n, 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""