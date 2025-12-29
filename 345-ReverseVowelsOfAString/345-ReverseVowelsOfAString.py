# Last updated: 29/12/2025, 03:03:06
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        vowels=set('aeiouAEIOU')  

        i, j = 0, len(s)-1

        while(i<j):
            if s[i] not in vowels:
                i+=1
            elif s[j] not in vowels:
                j-=1
            else:
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1
        return ''.join(s)
