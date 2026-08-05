# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        mid = head
        jumper = head
        while jumper.next and jumper.next.next:
            jumper = jumper.next.next
            mid = mid.next
        
        dummy = mid
        mid = mid.next
        dummy.next = None
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp

        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            second = temp2
            first = temp1




            

            