# Last updated: 31/12/2025, 18:43:50
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()

        minarrows = len(points)
        prev = points[0]

        for p in range(1, len(points)):
            curr = points[p]
            if curr[0] <= prev[1]:
                minarrows -= 1
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                prev = curr

        return minarrows