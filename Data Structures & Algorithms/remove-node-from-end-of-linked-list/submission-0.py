def nth(l, n):
    result = l
    for _ in range(n):
        result = result.next
    return result

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = nth(head, n)
        if not right:
            return head.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next if left.next else None
        return head