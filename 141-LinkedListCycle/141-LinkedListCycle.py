# Last updated: 29/12/2025, 03:03:36
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        """
        Understand
            Inputs - head of a singly linked list
            Outputs - True if there is a cycle in the list, else False
            Constraints - 0 <= number of nodes <= 10^4
                        -10^5 <= Node.val <= 10^5
                        pos is the index of the node where tail connects (-1 if no cycle)
            Examples/edge cases -
                []                        → False
                [1] with no cycle         → False
                [1] with cycle to itself  → True
                [3,2,0,-4] tail->2        → True
                [1,2] tail->0             → True

        Plan
            HL: Use Floyd’s Tortoise and Hare (fast/slow pointers).
                - Start both slow and fast at head
                - Move slow by 1 step, fast by 2 steps
                - If slow and fast meet → cycle exists (return True)
                - If fast reaches None → no cycle (return False)

        Time: O(n)   (each pointer moves at most n steps)
        Space: O(1)  (only two pointers used)
        """

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False



        