# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        prev , curr = None, second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev

        first, second = head, second

        while second:
            first_node = first.next
            second_node = second.next

            first.next = second
            second.next = first_node

            first = first_node
            second = second_node

        

        