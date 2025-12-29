# Last updated: 29/12/2025, 03:04:00
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        """
        Understand
            Input
                - A list of strings, e.g., ["eat","tea","tan","ate","nat","bat"]
            Output
                - A list of groups, where each group is a list of words that are anagrams of each other
            Constraints
                - 1 <= len(strs) <= 10^4
                - Each word has length up to 100
                - Words only contain lowercase English letters
            Edge cases
                - Input = [""] → output [[""]]
                - Input = ["a"] → output [["a"]]
                - Words with different lengths can never be anagrams
                - Large input sizes → efficiency matters

        Plan
            High-level idea
                - Two words are anagrams if, after sorting their letters, they look the same
                    Example: "eat", "tea", "ate" → sorted = "aet"
                - Use this sorted string as a "signature" (key) in a hashmap (dictionary).
                - Group words by their signature.

            Steps
                1. Create a dictionary (defaultdict of list) to hold groups.
                2. For each word in input:
                    - Sort the letters → make a key (e.g., "eat" → "aet").
                    - Append the original word into groups[key].
                3. Return all values from the dictionary as the final list of groups.

            Example
                Input = ["eat","tea","tan","ate","nat","bat"]
                - "eat" → key "aet" → groups["aet"] = ["eat"]
                - "tea" → key "aet" → groups["aet"] = ["eat","tea"]
                - "tan" → key "ant" → groups["ant"] = ["tan"]
                - "ate" → key "aet" → groups["aet"] = ["eat","tea","ate"]
                - "nat" → key "ant" → groups["ant"] = ["tan","nat"]
                - "bat" → key "abt" → groups["abt"] = ["bat"]
                Output = [["eat","tea","ate"],["tan","nat"],["bat"]]

        Alternative approach (character count)
                - Instead of sorting, count characters (26 slots for each letter).
                - Represent word as tuple of counts (e.g., "eat" → (1,0,1,...)).
                - Use this tuple as the dictionary key.
                - Advantage: avoids O(k log k) sorting step.
                - Useful when words are long.

        Time
            - Sorting method: O(n * k log k)
                n = number of words, k = average word length
            - Counting method: O(n * k) (faster for long words)

        Space
            - O(n * k) to store all words in groups
            - Extra space for dictionary keys
                - Sorting method: O(k) per key (depends on word length)
                - Counting method: O(26) = O(1) per key (fixed size)
        
        """

        groups = defaultdict(list)

        for word in strs:
            key = ' '.join(sorted(word))

            groups[key].append(word)

        return list(groups.values())
        