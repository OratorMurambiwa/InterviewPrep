# Last updated: 29/12/2025, 03:03:57
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
            Understand
                Input: nums (List[int]) — each element represents 
                    the maximum jump length you can make from that position.
                Output: True if you can reach the last index, False otherwise.
                Constraints:
                    1 ≤ len(nums) ≤ 10^4
                    0 ≤ nums[i] ≤ 10^5
                Examples:
                    [2,3,1,1,4] → True  (you can reach the end)
                    [3,2,1,0,4] → False (you get stuck at index 3)
                    [0] → True  (already at the goal)

            Plan 
                HL: Use a greedy strategy (forward traversal)
                    - Keep track of the farthest index we can currently reach 
                    (maxReach)
                    - Traverse each index i in nums:
                        • If i > maxReach → means we can’t reach this point → return 
                        False
                        • Else, update maxReach = max(maxReach, i + nums[i])
                    - If we finish the loop without getting stuck → return True

            Time:  O(n)
                We go through the list once, updating maxReach each time.

            Space: O(1)
                We only store one variable (maxReach).

        """

        maxjump = 0

        for i, jump in enumerate(nums):
            if i > maxjump:
                return False
            else:
                maxjump = max(maxjump, i + jump)

        return True 
            