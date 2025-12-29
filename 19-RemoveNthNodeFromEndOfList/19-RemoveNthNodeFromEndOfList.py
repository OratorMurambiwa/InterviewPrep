# Last updated: 29/12/2025, 03:04:10
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        """
        Understand
            Inputs - head of a singly linked list, integer n
            Outputs - head of the list after removing the nth node from the end
            Constraints -
                1 <= number of nodes <= 30
                1 <= n <= number of nodes
            Examples -
                [1,2,3,4,5], n=2 → [1,2,3,5]
                [1], n=1 → []
                [1,2], n=1 → [1]

        Plan
            HL: Use two pointers (fast & slow) with a gap of n nodes.

            1. Create a dummy node pointing to head:
                - Handles edge cases cleanly (like removing the head itself).
                - Initialize slow = dummy, fast = dummy.

            2. Move fast ahead by n+1 steps:
                - This ensures slow will stop just before the node to delete.

            3. Traverse both slow and fast until fast reaches None:
                - Move slow = slow.next, fast = fast.next.

            4. Delete nth node:
                - slow.next = slow.next.next
                - This skips the target node.

            5. Return dummy.next:
                - Skips the dummy and gives the new head.

        Time: O(n)   (one traversal of the list)
        Space: O(1)  (only two pointers)

        """


        D = ListNode(0, head)
        fast = slow = D

        for i in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return D.next
        