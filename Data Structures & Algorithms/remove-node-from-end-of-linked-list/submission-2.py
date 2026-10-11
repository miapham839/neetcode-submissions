# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        - Init slow to point at head, and fast to be n nodes ahead of slow
        - Increment slow and fast at the same rate
        - When fast reaches the end, slow is exactly the nth node from the end of the list
        - Involves removing a node --> use a dummy node to avoid removing head node edge case
        '''
        temp, prev = ListNode(-1), ListNode(-1)
        prev.next = temp
        temp.next = head
        slow, fast = temp, temp
        for i in range(1,n):
            fast = fast.next
        while fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next
        # Remove node at slow
        prev.next = prev.next.next
        return temp.next

