# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        back = head.next
        head.next = None
        while back != None:
            temp = back.next
            back.next = head
            head = back
            back = temp
        return head
            