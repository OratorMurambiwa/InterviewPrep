# Last updated: 31/12/2025, 18:43:45
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                previ, prevt = stack.pop()
                res[previ] = i - previ 

            stack.append((i, t))
        return res
        