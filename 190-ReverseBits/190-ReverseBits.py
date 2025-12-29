# Last updated: 29/12/2025, 03:03:28
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
            Understand
                Inputs - integer n (32-bit unsigned)
                Outputs - integer with bits reversed
                Constraints - exactly 32 bits
                Edge cases - leading zeros become trailing zeros after reversing

            Plan
                HL:
                1. Initialize rev = 0
                2. Repeat 32 times:
                - Extract last bit (n & 1)
                - Shift rev left by 1 (make space)
                - Add bit to rev (rev |= bit)
                - Shift n right by 1 (move to next bit)
                3. Return rev

            Time: O(1) — fixed 32 iterations
            Space: O(1) — uses constant space
        """

        rev = 0

        for i in range(32):
            bit = n & 1
            rev <<= 1
            rev |= bit
            n >>= 1
        return rev
 

        