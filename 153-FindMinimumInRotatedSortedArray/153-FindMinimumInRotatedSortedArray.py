# Last updated: 29/12/2025, 03:03:31
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Understand
            Problem: Given a rotated sorted array (no duplicates), 
                    find the smallest element in O(log n) time.
            Input  - nums (List[int]): sorted array rotated k times
            Output - Smallest integer in nums
            Example:
                [3,4,5,1,2] → 1
                [4,5,6,7,0,1,2] → 0
                [11,13,15,17] → 11 (already sorted)
            Constraints:
                1 ≤ len(nums) ≤ 5000
                -5000 ≤ nums[i] ≤ 5000
                nums has unique elements and is rotated.

        Plan
            HL: Use Binary Search
                - Initialize l = 0, r = len(nums) - 1, res = nums[0]
                - While l <= r:
                    • If current subarray nums[l:r] is sorted (nums[l] < nums[r]),
                    then the smallest is at nums[l]. Update res and break.
                    • Otherwise:
                        - Find mid = (l + r) // 2
                        - Update res = min(res, nums[mid])
                        - If nums[mid] >= nums[l]:
                            → Left half is sorted → search right → l = mid + 1
                        Else:
                            → Right half is sorted → search left → r = mid - 1
                - Return res

        Time:  O(log n)
            Binary search cuts the range in half each iteration.

        Space: O(1)
            Uses only constant extra variables (l, r, m, res).


        """


        res = nums[0]
        l, r = 0, len(nums) -1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res
        