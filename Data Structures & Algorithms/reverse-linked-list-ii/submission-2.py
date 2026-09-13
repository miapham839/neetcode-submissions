# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        # First pass:
        count = 0
        cur = head
        prev_left_node, left_node, right_node = None, None, None
        while cur:
            count += 1
            # If left = 1, count needs to be 0 in order for prev_left_node to be assigned. Which is not possible, so in that case it'll stay None
            if count == left - 1:
                prev_left_node = cur
            elif count == left:
                left_node = cur
            elif count == right:
                right_node = cur
            cur = cur.next
        # Reset cur = head for 2nd pass
        prev = left_node
        cur = prev.next
        while cur:
            if cur == right_node:
                nxt = cur.next
                cur.next = prev
                left_node.next = nxt
                if prev_left_node:
                    prev_left_node.next = cur
                    return head
                else:
                    return right_node
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt



        
        