# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        while head != None:
            dummy = head
            while dummy.next and dummy.next.next != None:
                dummy = dummy.next
            temp = dummy.next
            dummy.next = None
            dummy = temp

            temp = head.next
            head.next = dummy
            if head.next:
                head.next.next = temp
                head = head.next.next
            else: 
                head.next = temp
                head = head.next

            