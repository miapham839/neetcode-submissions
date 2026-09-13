# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        temp = ListNode()
        temp.next = head
        curr = temp
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:    
                curr = curr.next
        return temp.next
        