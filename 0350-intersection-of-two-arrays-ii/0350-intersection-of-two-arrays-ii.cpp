#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> intersect(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_map<int, int> counts;
        std::vector<int> result;
        
        // Step 1: Populate the map with frequencies from nums1
        for (int num : nums1) {
            counts[num]++;
        }
        
        // Step 2: Traverse nums2 and check against the map
        for (int num : nums2) {
            if (counts[num] > 0) {
                result.push_back(num);
                counts[num]--; // Decrement count to handle duplicates correctly
            }
        }
        
        return result;
    }
};