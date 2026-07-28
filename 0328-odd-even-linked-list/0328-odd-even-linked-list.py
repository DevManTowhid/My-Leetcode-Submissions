# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        p1 = dummy1
        p2 = dummy2
        temp = head
        i = 0

        while temp:
            if i == 0 or i % 2 == 0:
                p1.next = temp
                p1 = p1.next
            else:
                p2.next = temp
                p2 = p2.next

            temp = temp.next
            i += 1

        p1.next = dummy2.next
        p2.next = None

        return dummy1.next