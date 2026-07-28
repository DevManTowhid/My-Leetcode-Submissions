# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Dummy node acts as a pseudo-head for the sorted list
        dummy = ListNode(0)
        dummy.next = head
        
        prev = head  # Tail of the sorted sublist
        curr = head.next  # Unsorted node currently being evaluated
        
        while curr:
            # Optimization: if curr is greater than or equal to the tail of the
            # sorted sublist, it's already in the correct order.
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
            else:
                # Find the position to insert curr, starting from dummy
                prev_search = dummy
                while prev_search.next.val <= curr.val:
                    prev_search = prev_search.next
                
                # Detach curr from its current position
                prev.next = curr.next
                
                # Insert curr between prev_search and prev_search.next
                curr.next = prev_search.next
                prev_search.next = curr
                
                # Advance curr to the next unsorted node
                curr = prev.next
                
        return dummy.next

        