# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If input empty, return empty list
        if head == None:
            return None
        # Traverse and modify pointers accordingly
        previous = head
        current = previous.next
        previous.next = None
        while current:
            # Save next node
            nxt = current.next
            # Reverse pointer
            current.next = previous
            #  Update prev, cur
            previous = current
            current = nxt
        return previous
