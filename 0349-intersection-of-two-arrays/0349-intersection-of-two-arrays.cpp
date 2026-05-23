#include <vector>
#include <unordered_set>

class Solution {
public:
    std::vector<int> intersection(std::vector<int>& nums1, std::vector<int>& nums2) {
        // Use a set to store unique elements from nums1
        std::unordered_set<int> set1(nums1.begin(), nums1.end());
        std::unordered_set<int> resultSet;
        
        // Iterate through nums2 and check if the element exists in set1
        for (int num : nums2) {
            if (set1.count(num)) {
                resultSet.insert(num);
            }
        }
        
        // Convert the resultSet into a vector to return
        return std::vector<int>(resultSet.begin(), resultSet.end());
    }
};