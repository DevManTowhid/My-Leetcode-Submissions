# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def recursiveMaxrev(node):
            if not node.next:
                return [node.val, node]
            q = recursiveMaxrev(node.next)
            if q[0] > node.val:
                return [q[0],q[1]]
            else:
                node.next = q[1]
                return [node.val, node]
        
        return recursiveMaxrev(head)[1]