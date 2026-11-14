
class Solution:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        carry = 0
        while True:
            current.val += l1.val if l1 is not None else 0
            current.val += l2.val if l2 is not None else 0
            current.val += carry
            carry = current.val // 10
            current.val %= 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is None and l2 is None and carry == 0:
                break
            nextNode = ListNode()
            current.next = nextNode
            current = nextNode
        return result
        