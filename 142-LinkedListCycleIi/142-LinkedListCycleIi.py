# Last updated: 29/12/2025, 03:03:35
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Understand
            Inputs - head of a singly linked list
            Outputs - node where the cycle begins, or None if no cycle
            Constraints - 0 <= nodes <= 10^4
                        -10^5 <= Node.val <= 10^5
            Examples/edge cases -
                []                        → None
                [1] no cycle              → None
                [1] cycle to itself       → node 1
                [3,2,0,-4] tail->2        → node 2

        Plan
            HL: Use Floyd’s cycle detection in two phases:
                1. Detect cycle using fast/slow pointers
                2. When they meet, reset one pointer to head
                3. Move both step by step; the node where they meet = cycle start

        Time: O(n)   (at most 2 passes of list)
        Space: O(1)  (only two pointers)
        """
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        else:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

        