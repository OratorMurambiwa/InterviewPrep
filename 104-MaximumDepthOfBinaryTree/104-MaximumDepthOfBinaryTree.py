# Last updated: 29/12/2025, 03:03:45
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        """
            Understand
                Inputs - root node of a binary tree (or None if empty)
                Outputs - integer representing the max depth (longest path root → leaf)
                Constraints - tree can have up to ~10^4 nodes, values don’t affect depth
                Examples/edge cases -
                    • [] → 0
                    • [1] → 1
                    • [3,9,20,null,null,15,7] → 3

            Plan 
                HL: Use recursion:
                    - if node is None → depth = 0
                    - otherwise depth = 1 + max(depth(left), depth(right))

            Time: O(N) (we visit each node once)
            Space: O(H) recursion stack (H = height of tree, O(N) worst-case, O(log N) if balanced)
        """

        if not root:
            return 0

        left_depth = self.maxDepth(root.left)

        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

        