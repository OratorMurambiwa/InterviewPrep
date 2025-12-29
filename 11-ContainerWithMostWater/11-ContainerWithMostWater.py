# Last updated: 29/12/2025, 03:04:13
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        understand -
                    i - array of integers with heights
                    o - integer, max amount of water
                    c - no slanting
                    e- 
        Hlp -
                set two pointers, left = o, right = len(height) - 1
                max_area = 0
                loop through while left < right
                length = min(height(left), height(right))
                width = right - left
                area = length times the width
                max_area = max(max_area, area)
                if height(left) < height(right)
                left += 1, else right -= 1
                return max_area
        """

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            length = min(height[left], height[right])
            width = right - left
            area = length * width
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
