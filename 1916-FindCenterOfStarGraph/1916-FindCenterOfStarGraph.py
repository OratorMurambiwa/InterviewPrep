# Last updated: 29/12/2025, 03:02:38
class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        """
            Understand
                Inputs - 
                    • edges: list of pairs [u, v] representing edges of the star graph
                Outputs - 
                    • The label (number) of the center node
                Constraints - 
                    • The graph is always a valid star (so exactly one center exists)
                Examples/edge cases -
                    • edges = [[1,2],[2,3],[4,2]] → 2 (2 is connected to all others)
                    • edges = [[1,3],[2,3]] → 3 (3 is connected to 1 and 2)

            Plan
                HL:
                    1. Look at just the first two edges.
                    2. The center must appear in **both of them**.
                    3. Compare edges[0][0], edges[0][1] with edges[1][0], edges[1][1].
                    4. Return the one that matches.

            Time: O(1)  (only checks 2 edges)
            Space: O(1)

        """

        a, b = edges[0]
        c, d = edges[1]

        if a==c or a==d:
            return a
        return b
        



