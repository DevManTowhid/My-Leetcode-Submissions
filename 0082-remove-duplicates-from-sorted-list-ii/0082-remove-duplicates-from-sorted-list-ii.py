# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Step 1: Create a sentinel node to handle head deletion cleanly
        sentinel = ListNode(0, head)
        
        # 'prev' will always point to the last known distinct node
        prev = sentinel
        
        while head:
            # Step 2: Check if current node is the start of a duplicate sublist
            if head.next and head.val == head.next.val:
                # Move 'head' until we reach the last node of the duplicates
                while head.next and head.val == head.next.val:
                    head = head.next
                
                # Skip all duplicates by linking prev to the node AFTER the last duplicate
                prev.next = head.next
            else:
                # No duplicate detected, advance 'prev' to 'head'
                prev = prev.next
                
            # Move ahead in the list
            head = head.next
            
        return sentinel.next