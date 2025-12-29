# Last updated: 29/12/2025, 03:03:04
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        """
            Understand
                    Inputs -
                        • a, b: integers (can be positive, negative, or zero)
                    Outputs -
                        • Integer sum of a and b, computed without using '+' or '-'
                    Constraints -
                        • Must only use bitwise operations
                        • Works within a simulated 32-bit integer range
                    Examples/edge cases -
                        • (1, 2) → 3
                        • (5, -3) → 2
                        • (-1, 1) → 0
                        • (0, 0) → 0
                        • (-5, -2) → -7

                Plan
                    HL (Bitwise Addition Simulation):
                        1. Define mask = 0xFFFFFFFF (32-bit bitmask)
                            - Keeps only the lower 32 bits of results
                            - Simulates integer overflow behavior
                        2. While (b & mask) > 0:
                            - carry = (a & b) << 1 → bits where carry occurs
                            - a = a ^ b → adds bits without carry
                            - b = carry → prepare next round using the carry
                        3. When carry becomes 0, addition is complete.
                        4. Return result:
                            - If b > 0 (sum is positive), return a masked to 32 bits →
                             (mask & a)
                            - Else return a directly (handles negatives in Python)
                        5. This ensures consistent results even though Python integers
                         have no overflow.

                Time: O(1) — limited to 32-bit bit operations (constant loop count)
                Space: O(1)

                Real-World Uses
                    • Digital circuit design — simulates logic used by CPU adders
                    • CPU architecture and ALU (Arithmetic Logic Unit) operations
                    • Embedded systems where bit-level arithmetic is used for
                     efficiency
                    • Cryptography algorithms that rely on bitwise arithmetic
                    • Understanding two’s complement arithmetic for signed integers


        """
        # return sum([a,b])

        mask = 0xFFFFFFFF
        while (b&mask) > 0:
            a, b = (a^b), (a&b)<<1
        if b > 0:
            return (mask&a)
        else:
            return a
 
  
        