# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        first = []
        second = []
        temp1 = headA
        while temp1:
            first.append(temp1)
            temp1 = temp1.next
        temp2 = headB
        while temp2:
            second.append(temp2)
            temp2 = temp2.next

        m, n = len(first), len(second)
        matches = None
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if first[i] == second[j]:
                matches = matches + 1 if matches else 1
            if first[i] != second[j]:
                break
            i -= 1
            j -= 1
        def Llify(arr):
            head = ListNode(arr[0])

            temp = head

            for _ in range(1, len(arr)):
                temp.next = ListNode(arr[_])

                temp = temp.next
            return head

        if matches:
            matches = Llify(first[m - matches:])


        return matches.val if matches else None
        



        