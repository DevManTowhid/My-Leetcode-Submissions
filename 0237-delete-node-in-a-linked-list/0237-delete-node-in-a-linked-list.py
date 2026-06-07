class Solution:
    def deleteNode(self, node):
        # Copy the value of the next node into the current node
        node.val = node.next.val
        
        # Point the current node's next pointer to the node after the next
        node.next = node.next.next