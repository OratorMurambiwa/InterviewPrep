# Last updated: 29/12/2025, 03:04:08
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        Understand
            Inputs - a string s containing only '(', ')', '{', '}', '[' and ']'
            Outputs - True if s is valid, else False
            Constraints - 1 <= len(s) <= 10^4
            Examples/edge cases - "()", "()[]{}", "(]", "([)]", "{[]}"

        Plan 
            HL: Use a stack. Push opening brackets, pop when a matching closing is found. 
            If mismatch or leftover, return False.
            
        Time: O(n) (scan each character once)
        Space: O(n) (stack may store all characters if all are opening)
        """

        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                if not stack:
                    return False
                top_element = stack.pop()
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
        