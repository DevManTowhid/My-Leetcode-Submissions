# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        stack = []
        new_list = ListNode()
        iterator = new_list
        j = k
        while p:
            # print(p.val)
            
            # print(f"j is {j}")
            stack.append(p.val)
            p = p.next
            j -= 1
            if j == 0:
                segment_head = ListNode(stack.pop())
                segment_iter = segment_head
                # print(f"segment node is {segment_iter.val}")
                iterator.next = segment_head
                while stack:
                    node = ListNode(stack.pop())
                    # print(f"node is {node.val}")
                    segment_iter.next = node
                    
                    segment_iter = segment_iter.next
                    # print(f"segment node is {segment_iter.val}")
                j = k
                iterator = segment_iter
        
        while stack:
            node = ListNode(stack.pop(0))
            # print(f"node is {node.val}")
            segment_iter.next = node
                    
            segment_iter = segment_iter.next
            # print(f"segment node is {segment_iter.val}")
            j = k
            iterator = segment_iter

        p = new_list.next
        
        while p:
            # print(p.val)
            p = p.next
        
        return new_list.next