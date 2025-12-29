# Last updated: 29/12/2025, 03:04:03
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        """
                Understand
                    Inputs -
                        • candidates: list of distinct positive integers (e.g., [2,3,6,
                        7])
                        • target: integer value representing the desired sum (e.g., 7)
                    Outputs -
                        • A list of lists containing all unique combinations of 
                        candidates that sum to target
                    Constraints -
                        • You can use the same number multiple times.
                        • Order of numbers in each combination doesn’t matter.
                        • 1 ≤ len(candidates) ≤ 30
                        • 1 ≤ target ≤ 500
                    Examples -
                        • candidates = [2,3,6,7], target = 7 → [[2,2,3],[7]]
                        • candidates = [2,3,5], target = 8 → [[2,2,2,2],[2,3,3],[3,5]]
                        • candidates = [2], target = 1 → []

                Plan
                    HL (DFS + Backtracking):
                        1. Create an empty list `res` to store valid combinations.
                        2. Define a recursive function dfs(i, current, total):
                            - i: current index in candidates.
                            - current: current list of chosen numbers.
                            - total: current sum of chosen numbers.
                        3. Base Cases:
                            a) If total == target:
                                → Add a copy of current to res.
                            b) If total > target or i >= len(candidates):
                                → Stop exploring this path.
                        4. Recursive Choices:
                            • Include candidates[i]:
                                - Append it to current.
                                - Call dfs(i, current, total + candidates[i]).
                                - Pop it (backtrack) after exploring.
                            • Exclude candidates[i]:
                                - Move to next index → dfs(i + 1, current, total).
                        5. Start recursion with dfs(0, [], 0).
                        6. Return res at the end.

                Time: O(2^n) — exponential in worst case (each number can be included/
                excluded many times)
                Space: O(n) — recursion depth proportional to target size

                Real-World Uses
                    • Finding all coin combinations to make a given amount (coin 
                    change problem)
                    • Generating all ingredient mixes that reach a specific calorie or
                     cost target
                    • Creating all possible resource allocation plans that meet a 
                    fixed budget
                    • Solving puzzles or games where repeated selections are allowed 
                    (like dice sums)
                    • Backtracking foundations for algorithms in AI, optimization, and
                     search systems


        """
        res = []

        def backtrack(i, current, total):
            if total == target:
                res.append(list(current))
                return
            if i >= len(candidates) or total > target:
                return
                
            current.append(candidates[i])
            backtrack(i, current, total + candidates[i])
            current.pop()

            backtrack(i+1, current, total)

        backtrack(0, [], 0)
        return res


        