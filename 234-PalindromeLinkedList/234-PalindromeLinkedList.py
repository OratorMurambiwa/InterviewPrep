# Last updated: 29/12/2025, 03:03:18
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        """
        Understand
            Inputs - head of a singly linked list
            Outputs - True if list is a palindrome, False otherwise
            Constraints - 1 <= number of nodes <= 10^5
            Examples -
                [1, 2, 2, 1] → True
                [1, 2]       → False
                [1]          → True

        Plan
            HL: Use fast/slow pointers and in-place reversal to compare halves.

            1. Edge cases:
                - If list has 0 or 1 node, it’s automatically a palindrome.
            
            2. Find middle:
                - Use two pointers (slow, fast).
                - Move slow by 1, fast by 2.
                - When fast reaches end, slow will be at middle.
                - For odd-length lists, slow lands at exact middle (we reverse from there).
                - For even-length lists, slow lands at start of second half.

            3. Reverse second half:
                - Starting at slow, reverse links in-place until end.
                - This gives a reversed second half that can be compared forward.

            4. Compare halves:
                - Start one pointer at head (first_half).
                - Start another at the head of the reversed half (second_half).
                - Walk both pointers step by step.
                - If values ever differ → return False.
                - If all values match until second_half runs out → return True.

            5. (Optional) Restore list:
                - If required, reverse the second half again to restore original order.

        Time: O(n)   (each node is visited at most 3 times: middle-finding, reversing, comparing)
        Space: O(1)  (only pointers are used, no extra data structures)
        """

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, curr = None, slow
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        second_half = prev

        first_half, second_half = head, second_half
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True



        
        