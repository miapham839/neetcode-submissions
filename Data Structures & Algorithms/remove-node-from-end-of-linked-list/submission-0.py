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
        # Declare temp node -> point to head
        temp = ListNode()
        temp.next = head
        # Iterate over lst starting from temp node -> get length
        cur = temp
        length = 0
        while cur:
            length += 1
            cur = cur.next
        # Reset cur. Iterate over linked list second time
        cur = temp
        i = 1
        while cur:
            count = length - i
            # If count = n
            if count == n:
                # Point next pointer to the node after the next node
                nxt = cur.next
                cur.next = nxt.next
            # Increment i and cur pointer
            i += 1
            cur = cur.next
        return temp.next



