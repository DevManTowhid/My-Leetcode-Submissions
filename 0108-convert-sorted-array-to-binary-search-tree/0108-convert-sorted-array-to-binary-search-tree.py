class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build(left, right):

            # No elements available
            if left > right:
                return None

            # Middle element becomes root
            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            # Build left subtree
            root.left = build(left, mid - 1)

            # Build right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)