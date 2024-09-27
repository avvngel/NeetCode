#include <numeric>
#include <vector>
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum{std::accumulate(nums.begin(), nums.end(), 0)};
        if (sum & 1 != 0)
            return false;
        int target{sum/2};
        std::vector<bool> dp(target+1, false);
        dp[0] = true;
        for (int num : nums){
            for (int i = target; i > 0; --i){
                if (num <= i){
                    dp[i] = dp[i] || dp[i-num];
                }
            }
        }
        return dp[target];
    }
};

