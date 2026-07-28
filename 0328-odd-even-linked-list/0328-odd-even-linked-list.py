# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = []
        temp = head
        while temp:
            first.append(temp.val)
            temp = temp.next
        
        last = [first[p] for p in range(len(first)) if p % 2 == 0 ] + [first[p] for p in range(len(first)) if p % 2 == 1]
        
      

        root = ListNode(last[0]) if last else None
        temp = root
        for _ in range(1, len(last)):
            temp.next = ListNode(last[_])
            temp = temp.next

        return root
