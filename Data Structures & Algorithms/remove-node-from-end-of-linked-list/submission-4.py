# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length+=1
            current = current.next

        dummy = ListNode(0)
        dummy.next = head
        tail = dummy

        for i in range(length-n):
            tail = tail.next
        tail.next = tail.next.next
        return dummy.next
        