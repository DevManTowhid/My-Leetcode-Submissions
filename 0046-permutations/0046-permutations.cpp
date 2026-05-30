#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        permuteRecursive(nums, 0, result);
        return result;
    }

private:
    void permuteRecursive(vector<int>& nums, int start, vector<vector<int>>& result) {
        if (start == nums.size()) {
            // If we have reached the end of the array, add the current permutation to the result.
            result.push_back(nums);
            return;
        }

        // Iterate through each index starting from 'start' and swap elements to generate permutations.
        for (int i = start; i < nums.size(); ++i) {
            swap(nums[start], nums[i]); // Swap the elements.
            permuteRecursive(nums, start + 1, result); // Recurse with the next index.
            swap(nums[start], nums[i]); // Backtrack: Swap the elements back to the original position.
        }
    }
};
