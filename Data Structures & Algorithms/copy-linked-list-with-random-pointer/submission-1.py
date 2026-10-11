"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = dict()
        # Pointing to the original list
        cur = head

        # Dummy head node for the copied list
        temp = Node(0)
        cur_copy = temp
        while cur:
            # Check node
            node = None
            if cur not in nodes.keys():
                node = Node(cur.val)
                nodes[cur] = node
            else:
                node = nodes[cur]
            cur_copy.next = node
            cur_copy = cur_copy.next

            # Check random pointer
            if not cur.random:
                cur_copy.random = None
            else: 
                if cur.random not in nodes.keys():
                    node_rand = Node(cur.random.val)
                    nodes[cur.random] = node_rand
                else:
                    node_rand = nodes[cur.random]
                cur_copy.random = node_rand

            # Jump to the next node in the og list
            cur = cur.next

        return temp.next

