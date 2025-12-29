# Last updated: 29/12/2025, 03:03:13
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Understand
            Input
                - nums: list of n distinct numbers from the range [0..n]
                - Exactly one number in [0..n] is missing
            Output
                - The missing number (int)
            Constraints
                - 1 <= n <= 10^4 (sometimes larger)
                - nums contains distinct values only
            Edge cases
                - nums = [0] → missing 1
                - nums = [1] → missing 0
                - nums = [0,1,2] → missing 3
                - Large n: must handle efficiently

        Plan
            Three main approaches:

            1. Math Sum Formula
                - Expected sum of 0..n = (n * (n+1)) // 2
                - Actual sum = sum(nums)
                - Missing = expected_sum - actual_sum
                - Time: O(n)
                - Space: O(1)

            2. HashSet
                - Store all numbers in a set
                - Loop through 0..n, return the one not in the set
                - Time: O(n) (set lookup = O(1) average)
                - Space: O(n)

            3. XOR Trick
                - XOR all numbers from 0..n with all numbers in nums
                - Duplicates cancel out (a ^ a = 0)
                - Remaining value = missing number
                - Time: O(n)
                - Space: O(1)

        Example walkthrough (nums = [3,0,1], n=3)
            - Math sum:
                expected = (3*4)//2 = 6
                actual = 3+0+1 = 4
                missing = 6 - 4 = 2
            - HashSet:
                set = {0,1,3}
                check 0..3 → missing = 2
            - XOR:
                (0^1^2^3) ^ (3^0^1) = (2) → missing = 2

        Time
            - Math sum: O(n)
            - HashSet: O(n)
            - XOR: O(n)

        Space
            - Math sum: O(1)
            - HashSet: O(n)
            - XOR: O(1)
    """

        n = len(nums)
        result = 0

        for i in range(n + 1):
            result ^= i

        for num in nums:
            result ^= num

        return result


        