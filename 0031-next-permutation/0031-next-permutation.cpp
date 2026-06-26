#include <vector>
#include <algorithm>

class Solution {
public:
    void nextPermutation(std::vector<int>& nums) {
        int n = nums.size();
        int i = n - 2;
        
        // Step 1: Find the first decreasing element from the right (the pivot)
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        
        // Step 2: If a pivot was found, find the swap candidate
        if (i >= 0) {
            int j = n - 1;
            while (j >= 0 && nums[j] <= nums[i]) {
                j--;
            }
            // Swap the pivot with the candidate
            std::swap(nums[i], nums[j]);
        }
        
        // Step 3: Reverse the elements to the right of the pivot
        std::reverse(nums.begin() + i + 1, nums.end());
    }
};