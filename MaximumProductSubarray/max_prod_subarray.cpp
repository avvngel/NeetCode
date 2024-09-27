#include <algorithm>
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int global_max{nums[0]}
          , max_ending_here{1}
          , min_ending_here{1};

        for (int num : nums){
            int tmp = max_ending_here;
            max_ending_here = std::max({num, max_ending_here*num, min_ending_here*num});
            min_ending_here = std::min({num, tmp*num, min_ending_here*num});
            global_max = std::max(global_max, max_ending_here);
        }
        
        return global_max;
    }
};

