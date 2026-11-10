# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        if head.next is None:
            return head
        
        before = head
        current = head.next
        before.next = None
        while current.next is not None:
            # print(f"before={before} current={current}")
            after = current.next
            current.next = before
            before = current 
            current = after
        current.next = before
        return current
