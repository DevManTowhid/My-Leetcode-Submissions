class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge cases
        if not head or left == right:
            return head

        # Standard reverse function
        def reverseList(node):
            prev = None
            current = node
            while current:
                current_next = current.next
                current.next = prev
                prev = current
                current = current_next
            return prev

        # 1. Create a dummy node to handle the left == 1 edge case gracefully
        dummy = ListNode(0)
        dummy.next = head
        
        # 2. Find the node right before the 'left' position
        first_part_tail = dummy
        for _ in range(left - 1):
            first_part_tail = first_part_tail.next
            
        # 3. Identify the head of the sublist to be chopped
        chopped_head = first_part_tail.next
        
        # 4. Find the tail of the sublist to be chopped
        temp = chopped_head
        for _ in range(right - left):
            temp = temp.next
            
        # 5. Save the node that comes AFTER our chopped sublist, then sever the connection
        chopped_tail_next = temp.next
        temp.next = None
        
        # 6. Reverse the sublist
        chopped_reverse = reverseList(chopped_head)
        
        # 7. Reconnect the first part to the newly reversed head
        first_part_tail.next = chopped_reverse
        
        # 8. Reconnect the new tail (which is just the old chopped_head!) to the rest of the list
        chopped_head.next = chopped_tail_next

        # Return the actual head of the list (bypassing the dummy node)
        return dummy.next