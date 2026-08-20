# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy
        total = 0
        carry = 0
        digit_to_record = 0

        while l1 or l2 or carry:
            digit1 = 0 if l1 is None else l1.val
            digit2 = 0 if l2 is None else l2.val

            total = digit1+digit2+carry
            carry = total//10
            digit_to_record = total%10

            tail.next = ListNode(digit_to_record)
            tail = tail.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return dummy.next

            

        
        