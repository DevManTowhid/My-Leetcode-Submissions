/**
 * Definition for singly-linked list.
 * struct ListNode {
 * int val;
 * ListNode *next;
 * ListNode() : val(0), next(nullptr) {}
 * ListNode(int x) : val(x), next(nullptr) {}
 * ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        // Create two dummy nodes to act as the starting points of our two lists
        ListNode lt(0); 
        ListNode gte(0);
        
        // Pointers to build the lists
        ListNode* ltTmp = &lt;
        ListNode* gteTmp = &gte;
        
        ListNode* tmp = head;
        
        // Traverse the original list
        while (tmp != nullptr) {
            if (tmp->val < x) {
                // Add to the "less than" list
                ltTmp->next = tmp;
                ltTmp = ltTmp->next;
            } else {
                // Add to the "greater than or equal" list
                gteTmp->next = tmp;
                gteTmp = gteTmp->next;
            }
            // Move to the next node in the original list
            tmp = tmp->next;
        }
        
        // CRITICAL: Terminate the 'gte' list to prevent cycles in the linked list
        gteTmp->next = nullptr;
        
        // Connect the end of the 'less than' list to the start of the 'gte' list
        // We use gte.next to skip the dummy node itself
        ltTmp->next = gte.next;
        
        // Return the head of the newly partitioned list (skipping the lt dummy node)
        return lt.next;
    }
};