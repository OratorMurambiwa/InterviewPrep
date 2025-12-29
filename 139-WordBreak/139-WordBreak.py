# Last updated: 29/12/2025, 03:03:40
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """
        Understand
        Inputs
            - A string s (example: "leetcode")
            - A list of words wordDict (example: ["leet","code"])
        Output
            - True or False (can we cut up the string into pieces so every piece is in wordDict?)
        Constraints
            - String length is up to 300 (not too huge, so DP is okay)
            - WordDict can have up to 1000 words
        Edge cases
            - If s is "" (empty string), answer is True (empty string is trivially segmented).
            - If wordDict is empty, answer is False unless s is also empty.
            - Cases where many overlapping options exist (e.g., "catsanddog" with ["cats","dog","sand","and","cat"]).

    Plan
        High-level steps:
            1. Create a list dp where dp[i] means:
            "Can I break the substring s[0:i] into words from the dictionary?"
            (Substring from start up to i but not including i.)
            2. Start with dp[0] = True (the empty string is always valid).
            3. For each position i in the string (from 1 to n):
                - Look at all earlier cut positions j (0 to i-1).
                - If dp[j] is True AND s[j:i] (the slice from j to i) is in wordDict,
                then dp[i] = True (because we found a valid way to break it).
                - Break early if we already found a match for dp[i].
            4. At the end, check dp[n]. If it is True, then the whole string can be segmented.

    Example Walkthrough ("leetcode", ["leet","code"])
            - dp[0] = True
            - At i=4 → s[0:4] = "leet" in wordDict → dp[4] = True
            - At i=8 → s[4:8] = "code" in wordDict and dp[4] = True → dp[8] = True
            - Answer: dp[8] = True → "leetcode" can be split.

    Time
        - O(n^2) where n = length of s
        (Because for each i we check all j < i.)
    Space
        - O(n) for the dp list
    """
        wordset = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        
        return dp[n]


        