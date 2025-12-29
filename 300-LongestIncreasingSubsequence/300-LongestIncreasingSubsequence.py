# Last updated: 29/12/2025, 03:03:09
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
            Understand
                Inputs -
                    • nums: list of integers
                Outputs -
                    • Integer representing the length of the longest strictly 
                    increasing subsequence
                Examples -
                    • [10,9,2,5,3,7,101,18] → 4 ([2,3,7,101])
                    • [0,1,0,3,2,3] → 4 ([0,1,2,3])
                    • [7,7,7,7] → 1 ([7])
                Constraints -
                    • 1 ≤ len(nums) ≤ 2500
                    • -10⁴ ≤ nums[i] ≤ 10⁴

            Plan
                HL (Dynamic Programming):
                    1. Create dp[] of size len(nums), filled with 1s
                    2. For each i:
                        For each j < i:
                            - If nums[i] > nums[j], dp[i] = max(dp[i], dp[j] + 1)
                    3. Return max(dp)

            Time: O(n²)
            Space: O(n)

            Real-World Uses
                • Stock analysis: longest streak of price increases
                • Machine learning: detecting monotonic growth patterns
                • Scheduling: longest chain of tasks with increasing deadlines
                • Bioinformatics: finding growth patterns in DNA sequences
                • Data compression and sequence alignment problems

                do the o(nlogn solution)


        # """
        # dp = [1]*len(nums)

        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)

        tails = []

        for num in nums:
            index = bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num

        return len(tails)


        