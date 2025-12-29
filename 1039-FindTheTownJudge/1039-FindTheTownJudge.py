# Last updated: 29/12/2025, 03:02:50
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        """
        Understand
        Inputs - 
            • n: total number of people in the town (labeled 1 to n)
            • trust: a list of pairs [a, b] meaning person a trusts person b
        Outputs - 
            • The label (number) of the town judge if one exists, otherwise -1
        Constraints - 
            • The judge trusts nobody
            • Everyone else (n - 1 people) trusts the judge
        Examples/edge cases - 
            • n = 3, trust = [[1,3],[2,3]] → 3 (person 3 is the judge)
            • n = 3, trust = [[1,3],[2,3],[3,1]] → -1 (no judge)
            • n = 1, trust = [] → 1 (one person, no trust = judge)

        Plan 
        HL:
            1. Create a list trust_score of size n + 1 (index 0 unused).
            2. For each [a,b] in trust:
                - Decrease trust_score[a] by 1 (a trusts someone)
                - Increase trust_score[b] by 1 (b is trusted)
            3. Loop from 1 to n:
                - If trust_score[i] == n - 1:
                    return i (this is the judge)
            4. If no such person, return -1.

        Time: O(n + t), where t = number of trust relationships
        Space: O(n)
        """
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1
            score[b] += 1

        for i in range(1, n + 1):
            if score[i] == n -1:
                return i
        return -1
        