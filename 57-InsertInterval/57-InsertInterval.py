# Last updated: 29/12/2025, 03:03:55
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        """
            Understand
                Inputs
                    - intervals: list of sorted, non-overlapping [start, end] pairs
                    - newInterval: single interval [start, end] to insert
                Outputs
                    - list of merged, non-overlapping intervals after inserting 
                    newInterval

                Constraints
                    • intervals are sorted by start time
                    • 0 <= len(intervals) <= 10^4
                    • start_i <= end_i
                    • Must merge any overlaps caused by newInterval

            Plan
                HL:
                1. Create an empty list `res` for the final result.
                2. Loop through each interval:
                    a. If newInterval ends before current interval starts:
                            → add newInterval to res
                            → replace newInterval with current interval
                    b. Else if newInterval starts after current interval ends:
                            → add current interval to res
                    c. Else (overlap occurs):
                            → merge intervals by:
                                newInterval.start = min(newInterval.start, current.
                                start)
                                newInterval.end   = max(newInterval.end, current.end)
                3. After the loop, append the final newInterval (the last merged 
                interval).
                4. Return res.

            Time:  O(n)   — single pass through intervals
            Space: O(n)   — result list storage
        """

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                newInterval = intervals[i]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max (intervals[i][1], newInterval[1])

        res.append(newInterval)
        return res

        