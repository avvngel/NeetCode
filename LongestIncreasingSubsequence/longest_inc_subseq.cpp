#include <algorithm>
#include <vector>
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int max_len{1};
        std::vector<int> dp(nums.size(), 1);
        for (int i = nums.size()-2; i >= 0; --i){
            for (int j = i+1; j < nums.size(); ++j){
                if (nums[i] < nums[j]){
                    dp[i] = std::max(dp[i], 1 + dp[j]);
                    max_len = std::max(max_len, dp[i]);
                }
            }
        }
        return max_len;
    }
};

