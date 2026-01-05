# Last updated: 04/01/2026, 21:14:59
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = defaultdict(int)

        for char in s:
            freq[char] += 1
        
        length = 0
        odd = False

        for count in freq.values():
            if count % 2 == 0:
                length += count
            else:
                length += count -1
                odd = True
        
        if odd:
            return length + 1
        else:
            return length


        