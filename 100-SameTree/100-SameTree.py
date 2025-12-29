# Last updated: 29/12/2025, 03:03:52
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
    #all the nodes are the same and the structures are also the same
    #check if the roots are the same, if they are then check child nodes
    #if not return false
    #recursively search through the rest of the nodes

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # p = [1,2,3]
    # q = [1,2,3]

        