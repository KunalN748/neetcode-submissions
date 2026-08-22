# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            dummy = dummy.next
            length += 1
        dummy = head
        count = length - n - 1
        if count < 0:
            head = head.next
            return head
        while count > 0:
            dummy = dummy.next
            count -= 1
        dummy.next = dummy.next.next
        return head
