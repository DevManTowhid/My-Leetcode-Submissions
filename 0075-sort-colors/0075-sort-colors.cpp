#include <vector>
#include <algorithm> // Required for std::swap

class Solution {
public:
    void sortColors(std::vector<int>& nums) {
        int low = 0;
        int mid = 0;
        int high = nums.size() - 1;
        
        // Use a while loop because the pointers dictate when the pass is finished
        while (mid <= high) {
            if (nums[mid] == 0) {
                std::swap(nums[low], nums[mid]);
                low++;
                mid++;
            } 
            else if (nums[mid] == 1) {
                mid++;
            } 
            else { // nums[mid] == 2
                std::swap(nums[mid], nums[high]);
                high--;
                // Notice we do NOT increment mid here, 
                // because the new element at mid needs to be evaluated next.
            }
        }
    }
};