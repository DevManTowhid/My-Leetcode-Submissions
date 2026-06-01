class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Pointer to the last valid element in nums1
        int i = m - 1; 
        
        // Pointer to the last element in nums2
        int j = n - 1; 
        
        // Pointer to the very end of nums1 (the last empty slot)
        int k = m + n - 1; 

        // Compare elements from the back and place the largest at the end
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k] = nums1[i];
                i--;
            } else {
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }

        // If nums2 still has elements left, copy them over.
        // (Note: If nums1 has elements left, we don't need a loop for them 
        // because they are already sitting in their correct, sorted positions!)
        while (j >= 0) {
            nums1[k] = nums2[j];
            j--;
            k--;
        }
    }
};