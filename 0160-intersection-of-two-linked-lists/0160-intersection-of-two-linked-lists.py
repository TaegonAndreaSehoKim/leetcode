# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited_nodes = set()

        currA = headA
        
        while currA:
            visited_nodes.add(currA)
            currA = currA.next
        
        currB = headB
        
        while currB:
            if currB in visited_nodes:
                return currB
            currB = currB.next
        
        return None