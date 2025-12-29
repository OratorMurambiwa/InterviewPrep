# Last updated: 29/12/2025, 03:03:41
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = []

        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())

        return cleaned == cleaned[::-1]


      