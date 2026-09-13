# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Temporary head technique
        Declare temp node -> point to head
        Iterate over lst starting from temp node -> get length
        Set i = 1
        Iterate over lst, while curr is not None:
            count = length - (i += 1)
            if length = n:
                point next pointer to the node after the next node
        return temp.next
        '''
        # # Declare temp node -> point to head
        # temp = ListNode()
        # temp.next = head
        # # Iterate over lst starting from temp node -> get length
        # cur = temp
        # length = 0
        # while cur:
        #     length += 1
        #     cur = cur.next
        # # Reset cur. Iterate over linked list second time
        # cur = temp
        # i = 1
        # while cur:
        #     count = length - i
        #     # If count = n
        #     if count == n:
        #         # Point next pointer to the node after the next node
        #         nxt = cur.next
        #         cur.next = nxt.next
        #     # Increment i and cur pointer
        #     i += 1
        #     cur = cur.next
        # return temp.next

        '''
        - Time complexity: O(2n) = O(n)
        - Space complexity: O(1)
        '''
        '''
        Two Pointer method
        (+ Temporary head)
        Declare temp node -> point to head
        '''
        # Declare temp node -> point to head
        temp = ListNode()
        temp.next = head
        # Point left to dummy, right to head
        l = temp
        r = head
        # Move r up 2 steps
        i = 0
        while i < n:
            r = r.next
            i += 1
        # Move l and r at the same time
        while l and r:
            l = l.next
            r = r.next
        # At this point, r has reached the end. Because we have initial moved r such that the gap between 2 pointers is n, 
        # l is now exactly at the node before the node we have to remove.

        # Remove the node we want to remove
        l.next = l.next.next
        return temp.next


