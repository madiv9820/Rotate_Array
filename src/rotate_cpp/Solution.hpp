#pragma once
#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // Time Complexity: O(n^2), Space Complexity: O(1)
        // Ensure k is within the bounds of the array size
        // Rotating by the array's length or multiples of it results in the same array
        k = k % nums.size();
        
        // Perform the rotation k times
        for(int round = 1; round <= k; ++round) {
            // Store the last element since it will be moved to the front
            int lastElement = nums[nums.size()-1];
            
            // Shift all elements one position to the right
            // Start from the end to avoid overwriting values
            for(int index = nums.size()-1; index >= 1; --index)
                nums[index] = nums[index-1];
            
            // Place the previously last element at the beginning
            nums[0] = lastElement;
        }
    }
};