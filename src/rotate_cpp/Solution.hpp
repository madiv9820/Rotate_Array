#include <vector>
#include <functional>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();  // Get the size of the array
        k = k % n;            // Ensure k is within the bounds of the array length

        // Define a lambda function to reverse elements from index 'start' to 'end'
        function<void(int, int)> reverse = [&](int start, int end) -> void {
            for(; start < end; ++start, --end)
                swap(nums[start], nums[end]);  // Swap elements at positions start and end
        };

        reverse(0, n-1);  // Step 1: Reverse the entire array
        reverse(0, k-1);  // Step 2: Reverse the first k elements
        reverse(k, n-1);  // Step 3: Reverse the remaining n-k elements
    }
};