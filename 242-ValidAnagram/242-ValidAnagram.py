# Last updated: 29/12/2025, 03:03:12
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        Understand
        Inputs
            - Two strings s and t
        Output
            - Boolean: True if t is an anagram of s, False otherwise
        Constraints
            - 1 <= len(s), len(t) <= 50,000
            - Strings contain only lowercase English letters
        Edge cases
            - If lengths differ → immediately False
            - If both are empty "" and "" → True
            - If s = "a", t = "a" → True
            - If s = "a", t = "b" → False

        Plan
        HL (two main ways):
            1. Sorting
                - Sort both strings and check if they are equal
            2. Hashmap (counting chars) → More efficient
                - Count frequency of each character in s
                - Count frequency of each character in t
                - If both counts are equal → True else False

        Example: s = "anagram", t = "nagaram"
            - Count s: {a:3, n:1, g:1, r:1, m:1}
            - Count t: {n:1, a:3, g:1, r:1, m:1}
            - Counts match → True

         Time
        - Sorting → O(n log n)
        - Hashmap → O(n)
        Space
        - Sorting → O(1) or O(n) depending on language
        - Hashmap → O(1) (since only 26 letters at most)
        """
        # return sorted(s) == sorted(t) 

        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in s:
                return False

            else:
                count[char] -= 1

            if count[char] < 0:
                return False

        return True


        