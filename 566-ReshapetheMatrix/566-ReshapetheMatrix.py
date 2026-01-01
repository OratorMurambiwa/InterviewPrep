# Last updated: 01/01/2026, 04:01:48
1class Solution(object):
2    def combinationSum(self, candidates, target):
3        """
4        :type candidates: List[int]
5        :type target: int
6        :rtype: List[List[int]]
7        """
8        res = []
9
10        def backtrack(i, current, total):
11            if total == target:
12                res.append(list(current))
13                return
14
15            if i >= len(candidates) or total > target:
16                return
17
18            current.append(candidates[i])
19            backtrack(i, current, total + candidates[i])
20            current.pop()
21
22            backtrack(i + 1, current, total)
23
24        backtrack(0, [], 0)
25        return res
26
27
28
29
30        