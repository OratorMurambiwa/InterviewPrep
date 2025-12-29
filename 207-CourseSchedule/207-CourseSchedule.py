# Last updated: 29/12/2025, 03:03:21
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[b].append(a)

        visiting = set()
        visited = set()
        

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True
