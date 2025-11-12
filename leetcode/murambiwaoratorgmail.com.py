# murambiwaorator@gmail.com
# https://neetcode.io/problems/search-insert-position?list=neetcode250
# Language: Python
# Difficulty: Unspecified

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m

            if nums[m] > target:
