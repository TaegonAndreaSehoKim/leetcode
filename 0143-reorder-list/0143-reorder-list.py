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
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        previous = None
        current = second
        first = head
        
        while current:
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node

        second = previous
        
        while second:
            first_next_node = first.next
            second_next_node = second.next
            
            first.next = second
            second.next = first_next_node

            first = first_next_node
            second = second_next_node
        