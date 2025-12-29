# Last updated: 29/12/2025, 03:03:02
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """
        Understand
            Input
                - s: a string of uppercase English letters
                - k: max number of characters we are allowed to replace
            Output
                - The length of the longest substring that can be turned into all the same letter
            Constraints
                - 1 <= len(s) <= 10^5
                - 0 <= k <= len(s)
            Edge cases
                - k = 0 → must already be repeating chars, no changes allowed
                - All chars the same → answer = len(s)
                - If k is very large (≥ len(s)), answer = len(s) because we can replace everything

        Plan
            High-level idea: Sliding Window
                - We want the largest window [left..right] where we can make the entire substring one
                 repeating char
                - Keep a count of characters inside the window
                - Track the maximum frequency of a single character in the window (max_count)
                - Window size = right - left + 1
                - To make the window uniform:
                    replacements_needed = window_size - max_count
                - If replacements_needed > k, window is invalid → shrink from left
                - Otherwise, update max_len with the current window size

            Example (s="AABABBA", k=1)
                Step 1: Expand window
                    right=0 → "A", max_count=1, window_size=1, valid
                    right=1 → "AA", max_count=2, window_size=2, valid
                    right=2 → "AAB", max_count=2, window_size=3, valid
                    right=3 → "AABA", max_count=3, window_size=4, valid → max_len=4
                    right=4 → "AABAB", max_count=3, window_size=5, replacements=2 > k → shrink → "ABAB"
                    continue process...
                Step 2: Final max_len = 4

        Time
            - O(n) because each char is added once and removed at most once
            - No nested loops, just sliding pointers

        Space
            - O(26) = O(1) for the frequency dictionary (fixed alphabet size)

        Key Insight
            - The trick is to only track max_count (most frequent char in window),
            instead of recalculating every time.
            - This guarantees we always know how many replacements are needed.
        """

        count = defaultdict(int)
        max_len = 0
        max_count = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            max_count = max(max_count, count[s[right]])
        

            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

        