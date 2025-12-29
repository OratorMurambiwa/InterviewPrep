# Last updated: 29/12/2025, 03:03:34
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        """
        Understand
            Inputs - head of a singly linked list
            Outputs - reorder the list in-place to follow the pattern:
                        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 …
            Constraints - 1 <= number of nodes <= 5 * 10^4
            Examples -
                [1,2,3,4]   → [1,4,2,3]
                [1,2,3,4,5] → [1,5,2,4,3]
                [1]         → [1]

        Plan
            HL: Break into 3 main steps → (1) find middle, (2) reverse second half, (3) merge halves.

            1. Edge cases
                - If the list has 0 or 1 node, no change is needed.

            2. Find the middle using fast & slow pointers
                - Initialize slow = head, fast = head.
                - Move slow by 1 step, fast by 2 steps each iteration.
                - When fast reaches the end, slow will stop at the middle.
                - This divides the list into two halves:
                    first half: head → … → slow
                    second half: slow.next → … → tail
                - Cut the list into two parts by setting slow.next = None.

            3. Reverse the second half
                - Take the head of the second half (slow.next before cutting).
                - Reverse links in-place until end of list.
                - After this, second_half points to the new head of the reversed list.

            4. Merge the two halves
                - Use two pointers: first (from head), second (from reversed second half).
                - While second is not None:
                    * Save first.next in tmp1 and second.next in tmp2.
                    * Link first.next = second.
                    * Link second.next = tmp1.
                    * Move first to tmp1 and second to tmp2.
                - This interleaves nodes from both halves like shuffling two decks of cards.

            5. End condition
                - Stop when the second half is exhausted.
                - The first half may have one extra node if the list length is odd (it just stays at the end).

        Time: O(n)   (traverse once to find middle + once to reverse + once to merge)
        Space: O(1)  (all operations are in-place, no extra data structures)
        """

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        second_half = prev

        first, second = head, second_half
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

