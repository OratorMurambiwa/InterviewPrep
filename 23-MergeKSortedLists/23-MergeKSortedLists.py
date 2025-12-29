# Last updated: 29/12/2025, 03:04:09

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        """
        Understand
            Inputs  - a list of k singly linked lists, each already sorted in ascending order
            Outputs - one merged sorted linked list containing all nodes
            Constraints -
                • 0 <= k <= 10^4
                • total number of nodes across all lists <= 10^5
                • -10^4 <= Node.val <= 10^4
            Examples -
                lists = [[1,4,5],[1,3,4],[2,6]]
                Output: [1,1,2,3,4,4,5,6]

                lists = []
                Output: []

                lists = [[]]
                Output: []

        Plan
            HL: Use a min-heap (priority queue) to always choose the smallest current node across all lists.

            1. Edge case:
                - If lists is empty, return None immediately.

            2. Initialize a min-heap.
                - For each list, if it is non-empty, push the first node into the heap.
                - Store each entry as (node value, list index, node) to avoid comparison errors when 
                values are equal.

            3. Create a dummy head node and a current pointer.
                - This dummy simplifies building the result list without worrying about the first node.
                - curr will always point to the tail of the merged list.

            4. While the heap is not empty:
                - Pop the smallest entry from the heap.
                - Attach this node to curr.next.
                - Move curr to this node.
                - If this node has a .next, push that .next node into the heap (so the list 
                continues to be represented).

            5. After processing all nodes, return dummy.next (skipping the placeholder).

        Time: O(N log k)
            - N = total number of nodes
            - k = number of lists
            - Each node is pushed and popped from the heap once, each heap operation costs log k
        Space: O(k) for the heap (plus O(1) extra pointers)

        Notes / Patterns:
            - Very similar to the "merge step" of merge sort, but extended to k lists instead of 2.
            - Dummy nodes + priority queues are common patterns for linked list merging problems.
        """

        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        head = ListNode()
        curr = head

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next

            if node:
                heapq.heappush(heap, (node.val, i, node))

        return head.next



        