# Last updated: 29/12/2025, 03:03:01
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        """
            Understand
                Inputs  - intervals: list of [start, end] pairs
                        e.g. [[1,2],[2,3],[3,4],[1,3]]
                Outputs - integer = minimum number of intervals to remove 
                        so that no two overlap

                Constraints
                    • 1 <= len(intervals) <= 10^5
                    • start < end for each interval
                    • intervals may overlap in any order

                Examples / Edge Cases
                    [[1,2],[2,3],[3,4],[1,3]] → 1
                    [[1,2],[1,2],[1,2]]       → 2
                    [[1,2],[2,3]]             → 0
                    [[1,100],[11,22],[1,11],[2,12]] → 2

            Plan
                HL:
                1. Sort intervals by start time (default sort() already does this).
                2. Keep track of:
                    • prevEnd → end of the last non-overlapping interval
                    • counter → how many overlaps we remove
                3. Loop through each interval from the 2nd onward:
                    a. If current start >= prevEnd → no overlap → update prevEnd = end
                    b. Else (overlap) → increment counter by 1
                        and set prevEnd = min(prevEnd, end)
                        (we keep the one that ends earlier to reduce future overlaps)
                4. Return counter

            Time:  O(n log n)  (sorting dominates)
            Space: O(1)        (only uses a few variables)
        """

        intervals.sort()
        counter = 0

        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                counter += 1
                prevEnd = min(prevEnd, end)

        return counter
        