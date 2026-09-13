# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        - I: head of singly linked list
        - O: head of reversed list
        - E: empty lst -> return None

        Plan:
        - Traverse the list
        - At each node, point next pointer to the node before it
        - -> Keep track of prev node
        - Edge case: Head of lst with no prev node -> Use temporary head technique

        Pseudocode
        Init prev - point to None
        Init cur - point to head
        While cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
        '''
        # Edge case: Empty linked list
        if not head:
            return None
        # Init prev - point to None
        prev = None
        # Init cur - point to head
        cur = head
        # Traverse through linked list, reversing each node's next pointer
        while cur is not None:
            # Save next node ref
            nxt = cur.next
            # Reverse next pointer
            cur.next = prev
            # Update prev and cur pointers
            prev = cur
            cur = nxt
        # Return the new head (the tail of the original list) pointed to by prev
        return prev

    



        