# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find midpoint
        # TODO: Why different than checking cycle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Pointer to 2nd half
        l2 = slow.next
        slow.next = None

        # Reverse 2nd half
        prev = None
        cur = l2
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        l2 = prev

        # Traverse through the 2 lists node by node + update pointers
        l1 = head
        temp = ListNode()
        cur = temp
        while l1 and l2:
            cur.next = l1
            l1 = l1.next
            cur.next.next = l2
            l2 = l2.next
            cur = cur.next.next
        cur.next = l1 or l2

