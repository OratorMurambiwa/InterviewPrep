# Last updated: 29/12/2025, 03:02:48
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        """
                    Understand
                Inputs -
                    • text1: first string (e.g., "abcde")
                    • text2: second string (e.g., "ace")

                Outputs -
                    • Integer: length of the longest sequence of characters 
                    that appear in both strings in the same relative order 
                    (not necessarily consecutively)

                Constraints -
                    • 1 ≤ len(text1), len(text2) ≤ 1000
                    • Both strings contain only lowercase English letters

                Examples -
                    • text1 = "abcde", text2 = "ace" → 3 ("ace")
                    • text1 = "abc", text2 = "abc" → 3 ("abc")
                    • text1 = "abc", text2 = "def" → 0 (no match)

            Plan
                HL (Top-Down Recursion + Memoization):
                    1. Define recursive function lcs(i, j):
                        - Returns the LCS length between text1[i:] and text2[j:].
                    2. Base Case:
                        - If either string ends (i == len(text1) or j == len(text2)),
                         return 0.
                    3. Memoization:
                        - Use a dictionary 'memo' to store computed results for each 
                        (i, j).
                    4. Character Match:
                        - If text1[i] == text2[j]:
                            → add 1 (for this matching character)
                            → move diagonally (i+1, j+1)
                    5. Character Mismatch:
                        - If they don’t match:
                            → skip one char from either string and take max(
                                lcs(i+1, j),
                                lcs(i, j+1)
                            )
                    6. Store result in memo[(i, j)] and return it.
                    7. Start recursion from lcs(0, 0).

                Simplified Flow:
                    - Match → +1 + lcs(next, next)
                    - Mismatch → max(lcs(skip1), lcs(skip2))

            Time: O(m × n)
                • Each pair (i, j) computed once and stored.
            Space: O(m × n)
                • Due to recursion depth and memo storage.

            Key Lines Explained
                memo = {}              → cache to avoid recomputing subproblems.
                if text1[i] == text2[j]:
                    return 1 + lcs(i+1, j+1)
                                    → we add +1 because matching chars 
                                        contribute to LCS length.
                else:
                    return max(lcs(i+1, j), lcs(i, j+1))
                                    → skip one side and take the better option.

            Real-World Uses
                • DNA / protein sequence alignment (bioinformatics)
                • File diff and merge tools (like Git)
                • Plagiarism detection
                • Typo correction and spell-checking
                • Data comparison and version control systems


        """
        memo = {}

        def lcs(i,j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i,j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + lcs(i+1, j+1)

            else: 
                memo[(i, j)] = max(lcs(i+1, j), lcs(i, j+1))

            return memo[(i, j)]

        return lcs(0,0)
 
            





        