# Last updated: 29/12/2025, 03:03:58
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        """
            Understand
                Inputs
                    - intervals: list of [start, end] pairs (2D list)
                    e.g. [[1,3],[2,6],[8,10],[15,18]]
                Outputs
                    - list of merged, non-overlapping intervals
                    e.g. [[1,6],[8,10],[15,18]]

                Constraints
                    • 1 <= len(intervals) <= 10^4
                    • start_i <= end_i
                    • Intervals may overlap or touch
                    • Output must be sorted and have no overlaps

                Examples / Edge Cases
                    [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]
                    [[1,4],[4,5]]                → [[1,5]]
                    [[1,2]]                      → [[1,2]]
                    []                           → []

            Plan 
                HL:
                1. Handle empty list → return [] if no intervals.
                2. Sort intervals by start time using key=lambda x: x[0].
                3. Initialize merged = [intervals[0]] (list containing the first
                 interval).
                4. Loop through remaining intervals:
                    a. Compare current.start with merged[-1].end
                    b. If overlapping (start <= merged[-1].end):
                            merged[-1].end = max(merged[-1].end, current.end)
                    c. Else:
                            merged.append(current interval)
                5. Return merged list.

            Time:  O(n log n) — due to sorting
            Space: O(n)       — for the merged output list
        """

        intervals.sort()

        result = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = result[-1][1]
            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])
        return result
    

    
        