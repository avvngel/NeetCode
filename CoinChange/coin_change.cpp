#include <array>
#include <algorithm>
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        std::vector<int> dp(amount+1, amount+1);
        dp[0] = 0;
        for (int num = 1; num < amount+1; ++num){
            for (int coin : coins){
                if (0 <= num - coin){
                    dp[num] = std::min(dp[num], 1 + dp[num - coin]);
                }
            }
        }
        return dp[amount] == amount + 1 ? -1 : dp[amount];
    }
};

