class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        
        # Loop until pointers meet (either at the intersection node or at None)
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
            
        return pA