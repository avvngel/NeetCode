#include <algorithm>

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1)
            return nums[0];
        return std::max( rob2(nums.begin()+1, nums.end())
                       , rob2(nums.begin(), nums.end()-1));
    }
    
    template <typename Iterator>
    int rob2(Iterator begin, Iterator end) {
        int prev1{*(end - 1)}, prev2{0};
        for (auto it = end - 2; it != begin - 1; --it){
            int curr = std::max(*it + prev2, prev1);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
};

