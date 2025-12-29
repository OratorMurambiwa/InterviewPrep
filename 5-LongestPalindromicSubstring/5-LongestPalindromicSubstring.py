# Last updated: 29/12/2025, 03:04:21
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
                    Understand
        Inputs -
            • s: a string of lowercase or uppercase characters (1 ≤ len(s) ≤ 1000)
        Outputs -
            • The longest substring in s that is a palindrome (reads the same forward
             and backward)
        Constraints -
            • If multiple palindromes of the same length exist, return any one of them
            • Must return a contiguous substring (not subsequence)
        Examples/edge cases -
            • "babad" → "bab" or "aba"
            • "cbbd" → "bb"
            • "a" → "a"
            • "ac" → "a" or "c"
            • "aaaa" → "aaaa"

    Plan
        HL (Expand Around Center):
            1. Define a helper expand(l, r):
                - While l ≥ 0 and r < len(s) and s[l] == s[r]:
                    - Expand outward (l -= 1, r += 1)
                - Return the substring s[l+1:r] (the last valid palindrome)
            2. Initialize longest = ""
            3. For each index i in s:
                - odd = expand(i, i)        → handles odd-length palindromes ("aba")
                - even = expand(i, i + 1)   → handles even-length palindromes ("abba")
                - Update longest using: longest = max(longest, odd, even, key=len)
            4. Return longest at the end

    Time: O(n²)   — we expand around each character and compare characters outward
    Space: O(1)   — only store a few pointers and strings

    Real-World Uses
        • DNA and genome analysis — detecting mirrored or palindromic DNA sequences
        • Text and pattern recognition — finding symmetric word or character structures
        • Cryptography — detecting palindromic keys or symmetric message fragments
        • Data compression and error correction — identifying repeating/mirroring 
        patterns
        • Natural language processing — recognizing balanced or mirrored linguistic
         constructs


        """
        def check(l,r):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        longest = ''
        for i in range(len(s)):
            odd = check(i,i)
            even = check(i, i+1)
            longest = max(longest, even, odd, key=len)

        return longest
