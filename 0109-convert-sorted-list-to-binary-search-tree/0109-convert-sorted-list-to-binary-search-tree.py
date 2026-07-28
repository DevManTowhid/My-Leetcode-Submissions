class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 1. Convert the linked list to an array
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
            
        # 2. Build the BST using array indices
        def build_bst(left, right):
            if left > right:
                return None
            
            # Find the exact middle index
            mid = (left + right) // 2
            
            # Create the root node
            root = TreeNode(values[mid])
            
            # Recursively build subtrees using index bounds
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            
            return root
            
        return build_bst(0, len(values) - 1)