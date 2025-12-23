#include <vector>
#include <functional>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;

        function<void(int, int)> reverse = [&](int start, int end) -> void {
            for(; start < end; ++start, --end)
                swap(nums[start], nums[end]);
        };

        reverse(0, n-1);
        reverse(0, k-1);
        reverse(k, n-1);
    }
};