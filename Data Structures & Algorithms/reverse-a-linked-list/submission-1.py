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
        Init temp head node
        Point temp head to real head
        Init prev - point to temp head
        Init cur - point to head
        While cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return temp head.next
        '''
        # Edge case: Empty linked list
        if not head:
            return None
        # Init prev - point to head
        prev = None
        # Init cur - point to head.next
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
        return prev

    



        