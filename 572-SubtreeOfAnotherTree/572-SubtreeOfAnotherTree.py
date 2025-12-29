# Last updated: 29/12/2025, 03:02:58
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        """
            Understand
                Inputs - Two binary trees:
                        root (the larger tree), subRoot (the pattern tree).
                Outputs - Boolean: True if subRoot is a subtree of root, otherwise False.
                Constraints - Up to ~2e4 nodes; values may repeat; empty tree rules:
                            - empty subRoot is always a subtree
                            - non-empty subRoot cannot be inside empty root
                Examples/edge cases -
                    root = [3,4,5,1,2], subRoot = [4,1,2] -> True
                    root = [1,2,3], subRoot = [2] -> True
                    root = [1,2,3], subRoot = [4] -> False
                    root = None, subRoot = None -> True
                    root = None, subRoot = [1] -> False

            Plan 
                HL: Traverse root. At each node:
                    1) Check if root and subRoot are identical (helper isSame).
                    2) If not, recursively search the left subtree.
                    3) If not, recursively search the right subtree.
                Helper isSame checks full structural + value equality between two trees.

            Time: O(N * M) worst case (N = nodes in root, M = nodes in subRoot).
                - Each node in root could trigger a full scan of subRoot.
            Space: O(H) recursion stack (H = height of root tree).
                - Worst case O(N) for skewed trees, O(log N) if balanced.
        """
        if not subRoot:
            return True

        if not root:
            return False

        def issame(a,b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            return issame(a.left, b.left) and issame(a.right, b.right)

        return issame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)