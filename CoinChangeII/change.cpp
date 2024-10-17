#include <vector>

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        std::vector<int> prev(amount+1, 0);
        for (int i = coins.size()-1; i >= 0; --i){
            std::vector<int> dp(amount+1, 0);
            dp[0] = 1;
            for (int j = 1; j < amount+1; ++j){
                dp[j] = prev[j];
                if (j >= coins[i])
                    dp[j] += dp[j-coins[i]];
            }
            prev = dp;
        }
        return prev[amount];
    }
};

