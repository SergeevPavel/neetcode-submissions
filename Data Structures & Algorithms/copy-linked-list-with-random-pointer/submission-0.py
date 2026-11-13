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
        if head is None:
            return None
        result = Node(x=0)
        nodes = defaultdict(lambda: Node(x=0))
        nodes[head] = result
        current_origin = head
        current_result = result
        while current_origin is not None:
            current_result.val = current_origin.val

            if current_origin.next is not None:
                current_result.next = nodes[current_origin.next]
            
            if current_origin.random is not None:
                current_result.random = nodes[current_origin.random]

            # print(f"current_result: {current_result} {current_result.val} {current_result.next} {current_result.random}")
            current_origin = current_origin.next
            current_result = current_result.next
        return result
            
        