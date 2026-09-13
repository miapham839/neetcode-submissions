# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            if sum > 9:
                carry = int(str(sum)[0])
                cur.next = ListNode(int(str(sum)[1]), None)
            else:
                carry = 0
                cur.next = ListNode(sum, None)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        if l1:
            while l1:
                addition = l1.val + carry
                if addition > 9:
                    carry = int(str(addition)[0])
                    cur.next = ListNode(int(str(addition)[1]), None)
                else: 
                    carry = 0
                    cur.next = ListNode(addition, None)
                l1 = l1.next
                cur = cur.next
        if l2:
            while l2:
                addition = l2.val + carry
                if addition > 9:
                    carry = int(str(addition)[0])
                    cur.next = ListNode(int(str(addition)[1]), None)
                else: 
                    carry = 0
                    cur.next = ListNode(addition, None)
                l2 = l2.next
                cur = cur.next
        if (not l1 or l2) and (carry > 0):
            cur.next = ListNode(carry, None)
        return dummy.next

        