# Last updated: 29/12/2025, 03:04:04
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
            Understand
                Inputs  - nums: rotated sorted list of distinct integers
                        e.g., [4,5,6,7,0,1,2]
                        target: integer to find
                        e.g., 0
                Outputs - index of target if found, else -1

                Constraints - 
                    • O(log n) time required (must use binary search)
                    • Elements are distinct
                    • Array may be rotated (so only one half is sorted at a time)

                Examples / Edge Cases
                    nums = [4,5,6,7,0,1,2], target = 0 → output = 4
                    nums = [1,3], target = 3 → output = 1
                    nums = [1], target = 0 → output = -1
                    nums = [], target = 3 → output = -1

            Plan 
                HL:
                1. Initialize pointers l = 0, r = len(nums) - 1
                2. While l <= r:
                    a. Find mid index m = (l + r) // 2
                    b. If nums[m] == target → return m
                    c. Determine which half is sorted:
                        - If left half sorted (nums[l] <= nums[m]):
                            • If target lies in [nums[l], nums[m]), move r = m - 1
                            • Else move l = m + 1
                        - Else (right half sorted):
                            • If target lies in (nums[m], nums[r]], move l = m + 1
                            • Else move r = m - 1
                3. If loop ends, target not found → return -1

            Time:  O(log n) — each iteration halves the search space
            Space: O(1) — uses only constant extra variables (l, r, m)
        """


        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[r] >= target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
           
        
             
            
