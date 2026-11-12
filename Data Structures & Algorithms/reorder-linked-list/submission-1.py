# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = length(head)
        if l < 3:
            return
        prev_head2 = nth(head, l // 2 - 1)
        head2 = prev_head2.next
        prev_head2.next = None
        # print(f"head2: {head2}")
        head2 = reverse(head2)
        # print(f"head2 rev: {head2}")
        merge(head, head2)

def length(head):
    current = head
    result = 0
    while current is not None:
        result += 1
        current = current.next
    return result

def nth(head, n):
    current = head
    while n > 0:
        current = current.next
        n -= 1
    return current

def reverse(head):
    if head is None or head.next is None:
        return head
    prev = head
    current = head.next
    prev.next = None
    while True:
        # print(f"current: {current}")
        new_current = current.next
        current.next = prev
        prev = current
        if new_current is None:
            break
        current = new_current
    return current

def merge(head1, head2):
    proxy = ListNode()
    current = proxy
    while head1 is not None or head2 is not None:
        if head1 is not None:
            current.next = head1
            current = current.next
            head1 = head1.next
        if head2 is not None:
            current.next = head2
            current = current.next
            head2 = head2.next