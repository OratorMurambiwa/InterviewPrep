# Last updated: 29/12/2025, 03:03:27
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i == size - 1:
                    result.append(node.val)

        return result


        