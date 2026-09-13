# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        prev = None
        curr = head
        nxt = curr.next
        while curr:
            if nxt == None:
                curr.next = prev
                break
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = nxt.next
        return curr
        