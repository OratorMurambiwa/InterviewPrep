# Last updated: 29/12/2025, 03:02:39
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        """
            Understand
                Inputs -
                    • n: number of nodes labeled 0 to n-1
                    • edges: list of pairs [u, v] meaning undirected edge between u
                     and v
                    • source: starting node
                    • destination: target node
                Outputs -
                    • Boolean: True if a path exists from source to destination,
                     otherwise False
                Constraints -
                    • Graph is undirected
                    • Graph can be disconnected
                    • 1 <= n <= 2 * 10^5, so solution must be efficient
                Examples/edge cases -
                    • n = 3, edges = [[0,1],[1,2]], source = 0, destination = 2 → True
                    • n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, 
                    destination = 5 → False
                    • n = 1, edges = [], source = 0, destination = 0 → True (trivial 
                    case)

            Plan
                HL:
                    1. Build adjacency list from edges.
                    2. Use a DFS (recursive) function:
                        - If current node == destination → return True
                        - Mark node as visited
                        - Explore neighbors not visited yet
                        - If any neighbor path returns True → return True
                    3. If DFS finishes without finding destination → return False.

            Time: O(n + e), where e = number of edges (must visit all nodes and edges 
            at most once)
            Space: O(n + e) for adjacency list + visited set (recursion stack adds O
            (n) in worst case)


        """

        list1 = defaultdict(list)

        for a,b in edges:
            list1[a].append(b)
            list1[b].append(a)

        seen = set()

        def dfs(node):
            if node == destination:
                return True
                
            seen.add(node)

            for neighbor in list1[node]:
                if neighbor not in seen:
                    if dfs(neighbor):
                        return True
            return False

        
        return dfs(source)
        