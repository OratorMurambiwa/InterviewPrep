# Last updated: 29/12/2025, 03:02:54
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Understand
                Inputs -
                    • s: a string (1 ≤ len(s) ≤ 1000)
                Outputs -
                    • Integer: the total number of palindromic substrings in s
                Constraints -
                    • Substrings are contiguous
                    • Count all palindromes (not just distinct ones)
                Examples/edge cases -
                    • "abc" → 3  (each character)
                    • "aaa" → 6  ("a", "a", "a", "aa", "aa", "aaa")
                    • "aba" → 4  ("a", "b", "a", "aba")

            Plan
                HL (Expand Around Center):
                    1. Define a helper expand(l, r):
                        - While l ≥ 0 and r < len(s) and s[l] == s[r]:
                            - Increment a counter (found a palindrome)
                            - Expand outward (l -= 1, r += 1)
                    2. Initialize count = 0
                    3. For each index i in s:
                        - Expand for odd-length palindromes (center at i)
                        - Expand for even-length palindromes (center between i and i+1)
                    4. Return the total count

            Time: O(n²)  (we expand around each character)
            Space: O(1)  (just counters and pointers)

            Real-World Uses
                • DNA sequence symmetry detection (counting mirrored gene patterns)
                • Pattern analysis in strings (repetitions, palindromic segments)
                • Text mining — identifying symmetric or mirrored word patterns
                • Cryptography — analyzing symmetric substrings in encoded messages
        """
        
        def check(l, r):
            count = 0 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count +=1
                l -= 1
                r += 1
            return count

        total =0
        for i in range(len(s)):
            total += check(i,i)
            total += check(i, i+1)
        return total