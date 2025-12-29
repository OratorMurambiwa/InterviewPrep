# Last updated: 29/12/2025, 03:03:23
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """
        Understand
            Inputs - head of singly linked list
            Outputs - head of the list reversed
            Constraints - 0 <= nodes <= 5000
            Examples -
                [1,2,3,4,5] → [5,4,3,2,1]
                []          → []

        Plan
            1. Initialize two pointers:
                prev = None
                curr = head
            2. While curr is not None:
                - Save curr.next in next_
                - Redirect curr.next to prev (reverse the link)
                - Move prev forward to curr
                - Move curr forward to next_
            3. At the end, prev will point to the new head
            4. Return prev

        Time: O(n)   (visit each node once)
        Space: O(1)  (in-place reversal)
         """


        prev = None
        curr = head
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        return prev
        
        