# Last updated: 29/12/2025, 03:02:58
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        """
        Understand
            Inputs - nums (list of integers), k (integer window size)
            Outputs - maximum average value among all contiguous subarrays of length k
            Constraints - 1 <= k <= len(nums); must run efficiently (O(n) time)
            Edge cases - small arrays, all negatives, all positives, k == len(nums)

        Plan
            HL:
            1. Calculate the sum of the first k elements — this is the initial window.
            2. Store its average as the starting maximum (max_avg).
            3. Slide the window one step at a time:
            - Add the new incoming element (nums[i])
            - Subtract the outgoing element (nums[i - k])
            - Compute the new average
            - Update max_avg if the new average is higher
            4. Return the final max_avg after all windows are checked.

        Time: O(n) — each element is visited once.
        Space: O(1) — uses only a few extra variables.
    """

        n = len(nums)
        curr_sum = sum(nums[:k]) 
        max_avg = curr_sum / float(k)

        for i in range(k, n):
            curr_sum += nums[i] - nums[i - k]
            avg = curr_sum / float(k)
            max_avg = max(max_avg, avg)

        return max_avg



        