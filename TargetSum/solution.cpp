#include <algorithm>
#include <vector>
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int max_sum = std::accumulate(nums.begin(), nums.end(), 0);
        std::vector<int> prev(2*max_sum+1, 0);
        prev[max_sum] = 1;
        for (int i = 0; i < nums.size(); ++i){
            std::vector<int> dp(2*max_sum+1, 0);
            for (int j = 0; j < prev.size(); ++j){
                if (nums[i] <= j)
                    dp[j] += prev[j - nums[i]];
                if (j + nums[i] <= prev.size())
                    dp[j] += prev[j + nums[i]];
            }
            prev = dp;
        }
        return prev[max_sum + target];
    }
};

