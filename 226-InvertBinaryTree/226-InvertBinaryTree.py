# Last updated: 29/12/2025, 03:03:16
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        """
            Understand
            Inputs - root (TreeNode): the root of a binary tree. Can be None.
            Outputs - TreeNode: root of the binary tree after all left/right children
             are
            swapped
            Constraints - 
                • Each node has at most two children
                • Must handle edge cases like empty trees or trees with only one child

            Examples/Edge Cases -
                Input:        Output:
                1             1
                / \           / \
                2   3    =>    3   2
            / \               / \
            4   5             5   4

                - Input: None → Output: None
                - Input: 1 → Output: 1 (no children to swap)

        Plan 
            HL: Recursively traverse the tree. At each node:
                - Swap its left and right children.
                - Then call the same function on both children.

            Step-by-step:
            1. Base case: if root is None, return None
            2. Swap root.left and root.right
            3. Recursively call invertTree on the new root.left and root.right
            4. Return the root node (which now points to the inverted subtree)

        Time: O(n) – every node is visited once
        Space: O(h) – recursion stack depth, where h is the height of the tree
        """

        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root