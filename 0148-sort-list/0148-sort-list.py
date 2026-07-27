# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sortList(head):
            # Base case: If the list is empty or has only one node
            if not head or not head.next:
                return head

            # Step 1: Split the list into two halves using slow and fast pointers
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            mid = slow.next
            slow.next = None

            # Step 2: Recursively sort each half
            left = sortList(head)
            right = sortList(mid)

            # Step 3: Merge the two sorted halves
            return merge(left, right)

        def merge(l1, l2):
            dummy = ListNode()
            current = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

                # Append remaining nodes from either list
            current.next = l1 if l1 else l2

            return dummy.next

        return sortList(head)


        