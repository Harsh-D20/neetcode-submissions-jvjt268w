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
        def copy_helper(cur, node_map):
            if cur is None:
                return None, node_map
            next_node, node_map = copy_helper(cur.next, node_map)
            new_head = Node(cur.val, next=next_node)
            node_map.update({cur : new_head})
            return new_head, node_map

        new_head, node_map = copy_helper(head, {})
        cur, cur_old = new_head, head
        while cur and cur_old:
            cur.random = node_map[cur_old.random] if cur_old.random else None
            cur = cur.next
            cur_old = cur_old.next

        return new_head