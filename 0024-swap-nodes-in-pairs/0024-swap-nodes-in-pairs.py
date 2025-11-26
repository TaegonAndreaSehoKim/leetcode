# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(None)
        dummy.next = head

        prev = dummy
        curr = head

        while curr and curr.next:
            front = curr
            back = curr.next

            prev.next = back
            front.next = back.next
            back.next = front

            prev = front

            curr = front.next

        return dummy.next


