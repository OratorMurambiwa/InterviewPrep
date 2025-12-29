# Last updated: 29/12/2025, 03:03:39
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        """
                Understand
                Inputs -
                    • node: a reference to a node in an undirected, connected graph
                        - Each node has a value (val) and a list of neighbors
                Outputs -
                    • A deep copy (clone) of the graph starting from the input node
                Constraints -
                    • Graph is connected, so all nodes are reachable from input node
                    • Graph may contain cycles (e.g., node A connected to B, B back to
                     A)
                    • Must return new graph with no shared nodes with original
                Examples/edge cases -
                    • Input: 1--2, Output: cloned 1'--2'
                    • Input: 1--2--3--4 in a line, Output: cloned line graph
                    • Input: None (empty graph) → None
                    • Input: 1 connected to [2,4], 2 connected to [1,3], etc. (square 
                    cycle),
                    Output: cloned square cycle

            Plan
                HL:
                    1. Use a hashmap (dictionary) to store mapping of original node → 
                    cloned node.
                    2. Define DFS:
                        - If node already cloned, return its clone.
                        - Otherwise create a clone of current node.
                        - Recursively clone all neighbors and attach them.
                        - Return the clone.
                    3. Call dfs(node) and return its result.
                Notes:
                    • This avoids infinite recursion in cycles by checking hashmap 
                    first.
                    • Works because connected graph ensures traversal covers all nodes.

            Time: O(V + E), where V = number of nodes, E = number of edges
            Space: O(V) for hashmap + recursion stack

            Real-World Uses
                • Copying a social network (friend/follower graph) for simulation or 
                testing
                • Game development: cloning game maps or states for AI agents to 
                explore safely
                • Undo/redo systems in editors (cloning object graphs before change)
                • Compilers: cloning abstract syntax trees (ASTs) during code 
                transformations
                • Databases/knowledge graphs: duplicating subgraphs for experiments 
                without altering production


        """
        if not node:
            return None

        oldNew = {}

        def dfs(curr):
            if curr in oldNew:
                return oldNew[curr]

            copy = Node(curr.val)
            oldNew[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)


        